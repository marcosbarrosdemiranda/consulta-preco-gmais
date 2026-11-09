# Consulta Preço Gmais — Claude Code Guidelines

## Project Overview
Supermarket Price Check Kiosk system for Android tablets featuring a local FastAPI backend server integrating with the RP Info API.

## Key Architectural Rules & Constraints
1. **Authorized Sales Branches (Strictly 4 CNPJs)**:
   - `33168717000104` (Loja 001)
   - `33168717000449` (Loja 003)
   - `33168717000368` (Loja 010)
   - `33168717000791` (Loja 030)
   - Administrative units must be filtered out.

2. **RP Info API Token Caching & Optimization**:
   - **Crucial**: To prevent connection/session leaks (such as accumulating 80+ active sessions on the RP Info user account), the server implements in-memory token caching and global reuse (`get_rp_token` with expiration tracking and thread lock).
   - Reuses a single valid token across all store synchronizations, product lookups, and image requests until near expiration or 401 error.

3. **Local Database & Cache**:
   - SQLite (`produtos.db`) multi-store price isolation and compressed product image caching (`product_images`).

4. **Android Kiosk App & Versioning**:
   - Native Android Studio project (`android-kiosk/`) with auto-incrementing build versions (`version.properties`).
   - Dynamic screen orientation control (`AndroidBridge`), camera runtime permissions, and USB OTG barcode reader support.
