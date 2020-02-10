# engine
A very simple 3D engine

[![Build Status](https://travis-ci.org/Nachtfeuer/engine.svg?branch=master)](https://travis-ci.org/Nachtfeuer/engine)
[![Documentation](https://img.shields.io/badge/documentation-ok-brightgreen.svg)](https://nachtfeuer.github.io/engine/)
[![Coverage Status](https://coveralls.io/repos/github/Nachtfeuer/engine/badge.svg?branch=master)](https://coveralls.io/github/Nachtfeuer/engine?branch=master)
[![BCH compliance](https://bettercodehub.com/edge/badge/Nachtfeuer/engine?branch=master)](https://bettercodehub.com/)
[![codebeat badge](https://codebeat.co/badges/ddf9af2f-4072-43ab-82ed-f499ecdabbcd)](https://codebeat.co/projects/github-com-nachtfeuer-engine-master)
[![Known Vulnerabilities](https://snyk.io/test/github/Nachtfeuer/engine/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/Nachtfeuer/engine?targetFile=requirements.txt)
[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/Nachtfeuer/engine/?ref=repository-badge)

## Using mkdocs

```
pip install mkdocs pymdown-extensions plantuml-markdown
mkdocs build
mkdocs serve
```

If `mkdocs serve` does not work:

```
python -m http.server
```

## API Documentation

```
pip install pdoc3
pdoc --html -ohtml.docmentation engine
```

After this open html.documentation/engine/index.html in your browser.
As an alternative you can do following:

```
pdoc --http localhost:8000 engine
```

View http://localhost:8000 in your browser to see the API documentation.
You might have to use another port if that one is in use.

## Links

 - https://vvvv.org/documentation/3d-vector-mathematics
 - https://www.mathsisfun.com/algebra/vectors-cross-product.html
 - https://www.mathsisfun.com/algebra/vectors-dot-product.html
 - https://www.rapidtables.com/convert/number/radians-to-degrees.html
 - https://www.rapidtables.com/convert/number/radians-to-degrees.html
 - https://www.mathsisfun.com/algebra/matrix-multiplying.html
 - https://en.wikipedia.org/wiki/Rotation_matrix
 - https://docs.travis-ci.com/user/languages/python/
 - https://en.wikipedia.org/wiki/Vector_projection
 - https://pdoc3.github.io/pdoc/
 - http://www.ncsa.illinois.edu/People/kindr/emtc/quaternions/
 - http://www.ncsa.illinois.edu/People/kindr/emtc/quaternions/quaternion.c++
