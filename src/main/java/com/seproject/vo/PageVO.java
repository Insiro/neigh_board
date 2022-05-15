/*
PageableDefault 는 여러가지 단점이 있음
1. 페이지 번호가 0번 부터이기 때문에 사용자들에게는 직관적이지 않음
2. 파라미터를 이용하여 size 를 지정하기 때문에 고의적인 size 의 확대를 막을 수 없음
3. 기타 정렬방향이나 속성을 모든 브라우저에서 파라미터를 통해 조절할 수 있기 때문에고의적인 공격에 취약함

때문에 Value Object 를 생성하는 방식이 문제해결 방법임.
페이지 번호와 게시물의 수(size)만을 받도록 설계하고 제약을 걸어둠
정렬 방향이나 속성은 컨트롤러에서 지정함.
 */
package com.seproject.vo;


import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;

public class PageVO {
    private static final int DEFAULT_SIZE = 10;
    private static final int DEFAULT_MAX_SIZE = 50;

    private int page;
    private int size;

    private String keyword;
    private String type;

    public PageVO() {
        this.page = 1;
        this.size = DEFAULT_SIZE;
    }

    /*** Page 와 게시물의 수(size) ***/
    public int getPage() {
        return page;
    }

    public void setPage(int page) {
        this.page = page < 0 ? 1 : page;
    }

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size < DEFAULT_SIZE || size > DEFAULT_MAX_SIZE ? DEFAULT_SIZE : size;
    }

    public Pageable makePageable(int direction, String... props) {
        Sort.Direction dir = direction == 0 ? Sort.Direction.DESC : Sort.Direction.ASC;

        return PageRequest.of(this.page - 1, this.size, dir, props);
    }

    /*** type 과 keyword 수집 ***/
    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
}
