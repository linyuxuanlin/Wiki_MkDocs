`.github/workflows/ci.yml`:

```
name: ci 
on:
  push:
    branches:
      - main
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: 3.x
      - uses: actions/cache@v2
        with:
          key: ${{ github.ref }}
          path: .cache
      - name: Translate to Arabic
        env:  # 设置环境变量
          CHATGPT_API_KEY: ${{ secrets.CHATGPT_API_KEY }}
          CHATGPT_API_BASE: ${{ secrets.CHATGPT_API_BASE }}
        run: |
          pip install -r tools/requirements_translate.txt
          python tools/translate-to-ar-using-chatgpt.py || true
      - name: Commit translated
        run: |
          git pull
          git config --global user.email 824676271@qq.com
          git config --global user.name linyuxuanlin
          git commit -m "Commit translated" -a || true
      - name: Push changes
        uses: ad-m/github-push-action@master
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
      - run: pip install -r requirements.txt 
      - run: mkdocs gh-deploy --force
      

```