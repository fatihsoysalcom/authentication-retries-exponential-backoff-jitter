# Authentication Retries Exponential Backoff Jitter

This example demonstrates different strategies for handling transient authentication failures, a core concept discussed in the article about GitHub outages. It simulates a flaky authentication service and shows how a client behaves with no retries, naive retries, and a more robust exponential backoff with jitter retry mechanism. The goal is to illustrate how proper retry logic improves system resilience and prevents overwhelming the service.

## Language

`python`

## How to Run

Save the code as `main.py`.
Open a terminal or command prompt in the same directory.
Run the script using: `python main.py`

## Original Article

This example accompanies the Turkish article: [GitHub Kesintisi ve Kimlik Doğrulama Yeniden Denemelerinden Çıkarılan Dersler](https://fatihsoysal.com/blog/github-kesintisi-ve-kimlik-dogrulama-yeniden-denemelerinden-cikarilan-dersler/).

## License

MIT — see [LICENSE](LICENSE).
