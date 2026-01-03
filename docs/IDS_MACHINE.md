## Hypothèses machine IDS (typique labo)

- OS: Ubuntu/Debian x86_64
- CPU: 8–16 cores
- RAM: 32–64 GB
- Disk: ~1 TB SSD (pcaps + features)
- NIC: 1–2 (mgmt + capture/SPAN)

### Exécution Docker
- Offline: pcaps/datasets montés dans /data
- Live: host network + NET_RAW/NET_ADMIN (Linux host)
