# Deploying firstspindjbootcamp.org

This is a **static site in a subfolder** (`firstspindjbootcamp/`) of the
`Djrere7/Remixedevents` GitHub repo. It needs its **own** hosting project pointed at
that subfolder, on its **own** domain (separate from remixedeventsllc.com).

There is **no build step** — the host just serves the files. Paths are root-relative
(`/styles.css`, `/img/…`), so the publish root must be the `firstspindjbootcamp/` folder.

> Note: connecting the host to your account and changing DNS require your own login,
> so those steps must be done by you (or someone with account access). Everything in
> the repo is already configured — the steps below take ~5 minutes.

---

## Option A — Cloudflare Pages (recommended if the domain is on Cloudflare)

1. Cloudflare dashboard → **Workers & Pages → Create → Pages → Connect to Git**.
2. Pick the **Djrere7/Remixedevents** repo. Production branch: **main**.
3. Build settings:
   - **Framework preset:** None
   - **Build command:** *(leave empty)*
   - **Build output directory:** `firstspindjbootcamp`
   - (Root directory can stay `/`.)
4. **Save and Deploy.** You'll get a `*.pages.dev` preview URL.
5. **Custom domains → Set up a custom domain →** `firstspindjbootcamp.org`
   (and `www.firstspindjbootcamp.org`). If the domain is already on Cloudflare, records
   are added automatically. Otherwise Cloudflare shows the CNAME to add at your registrar.

`_headers`, `_redirects`, and the custom `404.html` are picked up automatically.

## Option B — Netlify

1. Netlify → **Add new site → Import an existing project → GitHub → Djrere7/Remixedevents**.
2. Build settings:
   - **Base directory:** `firstspindjbootcamp`
   - **Build command:** *(leave empty)*
   - **Publish directory:** `firstspindjbootcamp`
3. **Deploy.** You'll get a `*.netlify.app` URL.
4. **Domain management → Add a domain →** `firstspindjbootcamp.org`; Netlify shows the
   DNS records to add (apex A/ALIAS + `www` CNAME).

`netlify.toml`, `_headers`, `_redirects`, and `404.html` are all in this folder.

---

## DNS (at your domain registrar / DNS host for firstspindjbootcamp.org)
- **Cloudflare Pages:** add the domain as a Custom Domain in the Pages project; if the
  zone is on Cloudflare it auto-creates a CNAME (apex uses CNAME flattening).
- **Netlify:** point the apex per Netlify's panel (A record `75.2.60.5`, or ALIAS/ANAME to
  your `*.netlify.app`), and `www` as a CNAME to your `*.netlify.app`.
- Enable HTTPS (automatic on both hosts once DNS resolves).

## After it's live
- Every push to `main` auto-deploys.
- Set your live links/keys once in `main.js → FIRST_SPIN_CONFIG`
  (interest Google Form ✔, SpotFund donate ✔; add `formEndpoint` for on-page forms and
  `ga4MeasurementId` for analytics).
- Add real old→new redirects in `_redirects`.
