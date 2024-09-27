# CHANGELOG

## v0.4.0 (2024-09-27)

### Unknown

* Merge branch &#39;main&#39; of github.com:fleer/fastapi-server-template ([`2f8084c`](https://github.com/fleer/fastapi-server-template/commit/2f8084cbb5c124a595e310791ff8d98719ef0a7a))

## v0.3.0 (2024-09-18)

### Documentation

* docs(api.py): fixed Module name ([`ebeefcf`](https://github.com/fleer/fastapi-server-template/commit/ebeefcfd2f8235ffbeb756864ad963d1dbdaf988))

### Feature

* feat(prometheus): Added cpu and ram usage ([`6090a76`](https://github.com/fleer/fastapi-server-template/commit/6090a76e5ec076a960edcda40ea0b06cf1165cf1))

* feat: Prometheus, dev logging, config.dev.yaml ([`4a8865f`](https://github.com/fleer/fastapi-server-template/commit/4a8865f2233aa74d37b44df4e5071d0752f256a3))

### Refactor

* refactor: Moved tests to v1 ([`bec2f94`](https://github.com/fleer/fastapi-server-template/commit/bec2f94808954f79bec0a7831451ea41bebb3393))

### Unknown

* refactor:api Small corrections ([`1b0488e`](https://github.com/fleer/fastapi-server-template/commit/1b0488e61d91750b0cfdef67c4f2b3ab70a92d21))

* Merge branch &#39;main&#39; of github.com:fleer/fastapi-server-template ([`ac3240e`](https://github.com/fleer/fastapi-server-template/commit/ac3240e1a8c1546c3dcab633ea78dcf12a53df53))

## v0.2.1 (2024-07-15)

### Fix

* fix(routes): fixed routes ([`f93f1fe`](https://github.com/fleer/fastapi-server-template/commit/f93f1fee86f5cc69bc3a06f47861693afba06f83))

### Test

* test(router): fixed tests for /api/v1 ([`0ad9414`](https://github.com/fleer/fastapi-server-template/commit/0ad94145c008f2baebddebe3a9ab6bede168b880))

## v0.2.0 (2024-07-14)

### Unknown

* Merge branch &#39;main&#39; of github.com:fleer/fastapi-server-template ([`fb4d1f2`](https://github.com/fleer/fastapi-server-template/commit/fb4d1f23fb36cff872afcdcd1e1ddf6e45c19791))

## v0.1.1 (2024-07-12)

### Documentation

* docs(readme): improved service-repository pattern section ([`42f4bbd`](https://github.com/fleer/fastapi-server-template/commit/42f4bbdd59e4af6b9db8848c9c873a456545977e))

### Feature

* feat(repositpory/service): added repository and service layer ([`7b95f9a`](https://github.com/fleer/fastapi-server-template/commit/7b95f9a5b38aa5fa4ce2fba20fc1c96e37a8e063))

### Fix

* fix(conftest): finally fixed database creation problem ([`035ba64`](https://github.com/fleer/fastapi-server-template/commit/035ba64c0100b39e10fbd6e3c2a7d7553424da9b))

### Refactor

* refactor(routes): moved routes to v1 and changed code correspondingly

Fixed conftest and paths. Added info about repository and service layer ([`6332807`](https://github.com/fleer/fastapi-server-template/commit/633280730aad55a11ddb8cd63619e42a25be60ce))

### Unknown

* docs:config.py Added docs to config class ([`6e68cd1`](https://github.com/fleer/fastapi-server-template/commit/6e68cd184748313f152e532e68e9b387028a6edd))

* test:alembic Fixed problem with non-exisiting schemas

Added sleep to mitigate long creation processes ([`a681bbb`](https://github.com/fleer/fastapi-server-template/commit/a681bbbb70e0b9fb0f4acb45d749b897e1f43421))

* build:poetry plugin update ([`79550aa`](https://github.com/fleer/fastapi-server-template/commit/79550aa02f2a92659ef501224d155e6f7416997d))

* fix:db

Fixed DB schema definition and tests ([`e340578`](https://github.com/fleer/fastapi-server-template/commit/e34057866f96c0fd895920dedb755da375ef4679))

* docs:alembic

Added alembic to readme ([`1d1e2da`](https://github.com/fleer/fastapi-server-template/commit/1d1e2da51e9bdf492d062ab5cd644f30f627c69a))

* fix:alembic

Added schema creation ([`1f84c5f`](https://github.com/fleer/fastapi-server-template/commit/1f84c5fa132ec3221eb81c7896b2012c83d37405))

## v0.1.0 (2024-06-28)

### Ci

* ci(github actions): split workflows ([`660d180`](https://github.com/fleer/fastapi-server-template/commit/660d180dd360b853cced8235372d53600e684412))

* ci(github actions): added permissions ([`e5f8495`](https://github.com/fleer/fastapi-server-template/commit/e5f84954a7dc96a92f7227b5a322932a1fb13dd8))

* ci(githbub acrtions): no release ([`f0c0b63`](https://github.com/fleer/fastapi-server-template/commit/f0c0b63d96e9429c061417a2b86992f28509e5e3))

* ci(github actions): aligned trigger ([`88ff561`](https://github.com/fleer/fastapi-server-template/commit/88ff5618dd0cfbe8f3ab2f64bc933ba0639d283e))

* ci(github actions): aligned trigger

- push on main and release added ([`e6b5b59`](https://github.com/fleer/fastapi-server-template/commit/e6b5b595508f17d223b39853b98438929bab45a3))

* ci(github actions): fixed postgres envs in python_test.yaml ([`ad7237d`](https://github.com/fleer/fastapi-server-template/commit/ad7237db9d3ab53e2bdb870c7c0bd4a159f07a5b))

* ci(github actions): fixed python_test.yaml ([`7de2dc3`](https://github.com/fleer/fastapi-server-template/commit/7de2dc3237c4cbbc0e11581a3645d3d0898e437f))

* ci(github actions): fixed python_test.yaml again ([`442ef92`](https://github.com/fleer/fastapi-server-template/commit/442ef92d3bc9195a70d8d282b328c29957788db9))

* ci(github actions): fixed python_test.yaml ([`9e1b5f6`](https://github.com/fleer/fastapi-server-template/commit/9e1b5f6bb82659a4d9e941c569847b1bad1278ad))

* ci(github actions): fixed semantic_release.yaml ([`95eb79a`](https://github.com/fleer/fastapi-server-template/commit/95eb79aaf0e191f641b476c11f8a59d8d5604341))

### Documentation

* docs(readme.md): semantic Versioning added ([`3678977`](https://github.com/fleer/fastapi-server-template/commit/36789778189d66dd0e0837312d0e00f5089a40d6))

* docs(service): improved funtion docstrings ([`cfc5ee7`](https://github.com/fleer/fastapi-server-template/commit/cfc5ee7d761e1ffcf15168756ee5c795f1088ad4))

### Feature

* feat(added semantic release): - Package and workflow added ([`4402a0a`](https://github.com/fleer/fastapi-server-template/commit/4402a0aaa3a35117e32c2e2de4839066426d2665))

* feat(github actions): added github actions ([`88a9811`](https://github.com/fleer/fastapi-server-template/commit/88a981185c73bd385e9d53479d41068626dd0de3))

* feat(alembic): added database versioning tool

Alembic config added with working test ([`481662f`](https://github.com/fleer/fastapi-server-template/commit/481662f426b20c5e269d714517f98175ba95d80d))

* feat(template): added initial template stuff

pre-commit config
- poetry config
- pyproject.tom with ruff config ([`8b707cc`](https://github.com/fleer/fastapi-server-template/commit/8b707cc1a18f83c2ffc0adbd7dfb6d0ad87d75e7))

### Refactor

* refactor(service): general improvements and mkdocs ([`79115af`](https://github.com/fleer/fastapi-server-template/commit/79115afff3fcbc9fecc3a116d899e0e539399a90))

* refactor(service): moved package to src folder ([`6cc23c6`](https://github.com/fleer/fastapi-server-template/commit/6cc23c63d0fcc13f556b6809cbf7b2c5d4266a3d))

* refactor(service): improved config

Alle configurations are now handled via config.yaml ([`4cedc76`](https://github.com/fleer/fastapi-server-template/commit/4cedc7653cec389e956d6ab04219e3ca73d49328))

* refactor(config): improved database connection ([`230336e`](https://github.com/fleer/fastapi-server-template/commit/230336ece3a757f24863aed8d3405a625c062ffa))

### Test

* test(dataabse): added tests and fixed bugs ([`5a7f016`](https://github.com/fleer/fastapi-server-template/commit/5a7f016bb1ee5d0740e912380dfa65e2cc9a9690))

### Unknown

* Merge pull request #2 from fleer/Test

ci(github actions): aligned trigger ([`2eb9e76`](https://github.com/fleer/fastapi-server-template/commit/2eb9e76f9f451f4f43d9727ae697dffd5f63d993))

* Merge pull request #1 from fleer/Test

docs(readme.md): semantic Versioning added ([`7c1726b`](https://github.com/fleer/fastapi-server-template/commit/7c1726b3bf6235193b652780dfd248786b0d670d))

* Update pyproject.toml

Changed docstyle to google ([`6265923`](https://github.com/fleer/fastapi-server-template/commit/62659239b5a740293cd2a78af2b618f2ef81dbb2))

* First version of template ([`f37f567`](https://github.com/fleer/fastapi-server-template/commit/f37f5672e195c208a8adc9001b60c8790fd5c271))

* Update .pre-commit-config.yaml ([`bfb8df2`](https://github.com/fleer/fastapi-server-template/commit/bfb8df2cf5bf82c47f0d9606cba3ea8a82064239))

* Update .pre-commit-config.yaml ([`d916440`](https://github.com/fleer/fastapi-server-template/commit/d9164401b8e09e8a574824a7084cd05f4dc2a761))

* Initial commit ([`459475a`](https://github.com/fleer/fastapi-server-template/commit/459475a17d3126dc9905777240b4654836e1476c))
