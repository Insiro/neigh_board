# Project: Comment

# Introduction

manage Comment

# Overview

# Authentication

# Error Codes

# Rate limit

## End-point: addComment

### Method: POST

> ```
> http://{{host}}/post/{{postId}}/comment
> ```

### Body (**raw**)

```json
{
    "comment": "test1"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: Comment list

### Method: GET

> ```
> http://{{host}}/post/{{postId}}/comment
> ```
### Body (**raw**)

```json
{
    "comments": [
        {
            "post": "dbc227d4-192c-40f6-b100-6f5cbcd918e9",
            "author": "test",
            "comment": "test",
            "date": "2022-05-30",
            "id": "847ff9bd-d159-440b-a2fc-e0ceb5e4c667"
        }
    ]
}
```
⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: GetComment

### Method: GET

> ```
> http://{{host}}/comment/{{CommentId}}
> ```

### Body (**raw**)

```json
{
    "comment": {
        "post": "dbc227d4-192c-40f6-b100-6f5cbcd918e9",
        "author": "test",
        "comment": "test1",
        "date": "2022-05-30"
    }
}
```
⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

---

Powered By: [postman-to-markdown](https://github.com/bautistaj/postman-to-markdown/)
