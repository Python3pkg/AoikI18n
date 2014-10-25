# AoikI18n
A simple I18n solution featuring fallback locale, YAML locale file, synonym locale file, and flexible locale file path.

Tested working with:
- Python: 2.6+, 3.0+

[Package on PyPI](https://pypi.python.org/pypi/AoikI18n)

## Contents
- [How to install](#how-to-install)
  - [Install via pip](#install-via-pip)
- [How to use](#how-to-use)
  - [Import](#import)

  - [Force Unicode](#force-unicode)

  - [Create a YAML locale file](#create-a-yaml-locale-file)

  - [Create a synonym locale file](#create-a-yaml-locale-file)

  - [Create a path function](#create-a-path-function)

  - [Create an I18nObj object](#create-an-i18nobj-object)

  - [Create a tt function](#create-a-tt-function)

  - [Call the tt function](#call-the-tt-function)

## How to install

### Install via pip
Run
```
pip install AoikI18n
```
or
```
pip install git+https://github.com/AoiKuiyuyou/AoikI18n
```

## How to use

### Import
Class **I18n** contains static methods.  
Class **I18nObj** contains instance methods.  
```
from aoiki18n import I18n
from aoiki18n import I18nObj
```

[Example](https://github.com/AoiKuiyuyou/AoikBookmarksToFiles/blob/b8c5c4cf7ad7f00ab278d56177ffc578943b0200/src/aoikbookmarkstofiles/aoikbtf.py#L6) in code.

### Force Unicode
Force PyYAML to return Unicode values if you prefer so.
```
I18n.yaml_force_unicode()
```

[Example](https://github.com/AoiKuiyuyou/AoikBookmarksToFiles/blob/b8c5c4cf7ad7f00ab278d56177ffc578943b0200/src/aoikbookmarkstofiles/aoikbtf.py#L343) in code.

### Create a YAML locale file
[Example](https://github.com/AoiKuiyuyou/AoikBookmarksToFiles/blob/b8c5c4cf7ad7f00ab278d56177ffc578943b0200/src/aoikbookmarkstofiles/i18n/en.yml) in code.

### Create a synonym locale file
[Example](https://github.com/AoiKuiyuyou/AoikBookmarksToFiles/blob/b8c5c4cf7ad7f00ab278d56177ffc578943b0200/src/aoikbookmarkstofiles/i18n/en_us.yml) in code.

### Create a path function
AoikI18n does not prescribe any scheme for mapping from locale name to file path.  
It's up to the path function to implement the mapping.

This makes locale file path flexible.
>Simple things should be simple, complex things should be possible.

```
i18n_dir = os.path.join(os.path.dirname(__file__), 'i18n')

def path_func(locale):
    path = os.path.join(
        i18n_dir,
        locale + I18n.TT_FILE_EXT_STXT
    )
    return path
```

[Example](https://github.com/AoiKuiyuyou/AoikBookmarksToFiles/blob/b8c5c4cf7ad7f00ab278d56177ffc578943b0200/src/aoikbookmarkstofiles/aoikbtf.py#L371) in code.

### Create an *I18nObj* object
*locale* is the main locale.  
*locale2* is the fallback locale.  
*path_func* is defined [here](#create-a-path-function).

```
i18n = I18nObj(
    locale='zh',
    locale2='en',
    path_func=path_func,
    file_encoding='utf-8',
    load_file=True,
)

```

[Example](https://github.com/AoiKuiyuyou/AoikBookmarksToFiles/blob/b8c5c4cf7ad7f00ab278d56177ffc578943b0200/src/aoikbookmarkstofiles/aoikbtf.py#L385) in code.

### Create a tt function
**tt** means text transformation.

It's boring to write ```i18n.tt('key')``` everywhere.  
Instead, create a shorthand function.

```
tt = i18n.tt
```

[Example](https://github.com/AoiKuiyuyou/AoikBookmarksToFiles/blob/b8c5c4cf7ad7f00ab278d56177ffc578943b0200/src/aoikbookmarkstofiles/aoikbtf.py#L443) in code.

### Call the tt function
Call **tt** to map a key to a value in the main locale.  
If key is not found in the main locale, fallback will be used.  
If key is not found in the fallback locale either, return default or raise KeyError.
```
tt('key')
tt('key', default=None)
```

[Example](https://github.com/AoiKuiyuyou/AoikBookmarksToFiles/blob/b8c5c4cf7ad7f00ab278d56177ffc578943b0200/src/aoikbookmarkstofiles/aoikbtf.py#L499) in code.

That's it.
