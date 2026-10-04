"use strict";
/* Bump both names whenever SHELL_ASSETS or the fetch strategy changes, so the
 * activate handler cleanly drops the previous version's caches. */
const SHELL_CACHE = "gm-shell-v1";
const DATA_CACHE = "gm-data-v1";

const SHELL_ASSETS = [
  "./",
  "index.html",
  "profile.html",
  "brew.html",
  "compare.html",
  "finder.html",
  "offline.html",
  "manifest.json",
  "assets/js/profile-common.js",
  "assets/js/dialin-rules.js",
  "assets/js/finder-rules.js",
  "assets/js/pwa-register.js",
  "assets/icons/icon-192.png",
  "assets/icons/icon-512.png",
  "assets/icons/icon-maskable-512.png",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(SHELL_CACHE).then((cache) => cache.addAll(SHELL_ASSETS))
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches
      .keys()
      .then((keys) =>
        Promise.all(
          keys
            .filter((key) => key !== SHELL_CACHE && key !== DATA_CACHE)
            .map((key) => caches.delete(key))
        )
      )
      .then(() => self.clients.claim())
  );
});

self.addEventListener("message", (event) => {
  if (event.data?.type === "SKIP_WAITING") self.skipWaiting();
});

// Profile JSON, recipe/changelog markdown and the catalog must always prefer
// a fresh network copy — caching is only an offline fallback, never allowed
// to hide a profile update from someone who is actually online.
function isDataRequest(url) {
  return /\/profiles\//.test(url.pathname) && /\.(json|md|png)$/i.test(url.pathname);
}

async function networkFirst(request, cacheName) {
  const cache = await caches.open(cacheName);
  try {
    const response = await fetch(request);
    if (response.ok) cache.put(request, response.clone());
    return response;
  } catch (error) {
    const cached = await cache.match(request);
    if (cached) return cached;
    throw error;
  }
}

async function staleWhileRevalidate(request, cacheName) {
  const cache = await caches.open(cacheName);
  const cached = await cache.match(request);
  const fetchPromise = fetch(request)
    .then((response) => {
      if (response.ok) cache.put(request, response.clone());
      return response;
    })
    .catch(() => cached);
  return cached || fetchPromise;
}

self.addEventListener("fetch", (event) => {
  const url = new URL(event.request.url);
  if (url.origin !== self.location.origin) return; // never intercept GaggiMate LAN / cross-origin requests
  if (event.request.method !== "GET") return;

  if (event.request.mode === "navigate") {
    event.respondWith(
      (async () => {
        try {
          const response = await fetch(event.request);
          const cache = await caches.open(SHELL_CACHE);
          cache.put(event.request, response.clone());
          return response;
        } catch (error) {
          const cache = await caches.open(SHELL_CACHE);
          return (
            (await cache.match(event.request)) ||
            (await cache.match("offline.html")) ||
            Response.error()
          );
        }
      })()
    );
    return;
  }

  if (isDataRequest(url)) {
    event.respondWith(networkFirst(event.request, DATA_CACHE));
  } else {
    event.respondWith(staleWhileRevalidate(event.request, SHELL_CACHE));
  }
});
