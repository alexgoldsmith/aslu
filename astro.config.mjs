import path from "path";

import { fileURLToPath } from "url";

import { defineConfig } from "astro/config";

import { SITE } from "./src/config.mjs";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// https://astro.build/config
export default defineConfig({
  // Astro uses this full URL to generate your sitemap and canonical URLs in your final build
  site: SITE.domain,
  base: "/",
  bootstrap: '/node_modules/bootstrap',

  output: "static",

  integrations: [
  ],

  vite: {
    resolve: {
      alias: {
        "~": path.resolve(__dirname, "./src"),
      },
    },
  },
});
