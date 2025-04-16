# ethTrace 💡

**ethTrace** is a public REST API that enables real-time and historical analysis of Ethereum transaction flows based on geolocation, block height, token transfers, and contract activity. Built for developers, analysts, and researchers, ethTrace turns blockchain noise into actionable insights. 🚀📊🌍

---

## 🔍 Overview 🧭

Ethereum powers global decentralized finance — but understanding the **geographic flow** of ETH and tokens remains a challenge. ethTrace answers questions like: 💬

- Where is PYUSD or USDC flowing today?
- What regions are driving NFT or DeFi contract interactions?
- Which wallets are active in certain time zones?

ethTrace delivers a suite of endpoints powered by: 🛠️🔍🌍

- Public Etherscan API
- Google Cloud's Blockchain BigQuery datasets
- Lightweight geo-tagging and wallet tagging techniques

All wrapped in a blazing-fast FastAPI backend. ⚡🦄🚀

---

## 🧠 Features 📊

- 🌍 **Geographic Ethereum Flow Mapping**
- ⛽ **Token Volume & Transfer Trends**
- 🔗 **Contract Activity Insights**
- 🧠 **Known Wallet Labeling (e.g. merchant, CEX, NGO)**
- ⏳ **Real-Time + Historical Support**
- 🚀 **Simple REST API Interface**

---

## 📦 API Endpoints 📡📘🔗

### Flow Data

```
GET /flow?region=asia&hours=24
```

Returns aggregate transaction flow to/from a specified region in the past `n` hours.

### Token Volume

```
GET /token-volume?symbol=PYUSD
```

Returns estimated transfer volume for a given token symbol.

### Contract Trends

```
GET /top-contracts?limit=5
```

Returns top active contracts over the past 24 hours.

### Wallets by Tag

```
GET /wallets?tag=merchant&region=na
```

Returns labeled wallets active in a region or tag.

### Block Summary

```
GET /summary?block_range=latest
```

Returns summary stats for the latest block range.

---

## 🚀 How to Run 📦

### Requirements 🧰🧪📜

- Python 3.10+
- `fastapi`, `uvicorn`, `pandas`, `requests`, `google-cloud-bigquery`

### Run Locally 🚀

```bash
git clone https://github.com/mredidy/ethTrace.git
cd ethTrace
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 📺 Demo Video 🎥

A short walkthrough showing ethTrace in action, including endpoint queries, dashboard examples, and live deployment. 📈🧪🌍



---

## 📄 License 🔓

MIT License — See [LICENSE](./LICENSE) for details. 📜👐🛠️

---

## 🔗 Connect 🌐

- X (Twitter): [@mister\_edidy](https://x.com/mister_edidy)
- GitHub: [mredidy](https://github.com/mredidy)
- Discord: `mredidy`

---

## 🌍 Submission Info 🛠️

- Submitted to: **StackUp April 2025 Coding Challenge**
- Theme: **Build Your Own API**
- Focus: **Ethereum + Public Data + Geolocation**

Made with ❤️ by @mredidy 🚀🧑‍🚀✨

