package com.seproject.persistence;

import com.querydsl.core.BooleanBuilder;
import com.querydsl.core.types.Predicate;
import com.seproject.model.QWebBoard;
import com.seproject.model.WebBoard;
import org.springframework.data.querydsl.QuerydslPredicateExecutor;
import org.springframework.data.repository.CrudRepository;

// QuerydslPredicateExecutor 의 findAll() 은 Predicate 타입의 파라미터와 Pageable 을 파라미터로 전달 받습니다
// CrudRepository 파라미터 <T, ID> T 는 타입(WebBoard) ID 는 PK(Integer) 의 자료형
public interface WebBoardRepository extends CrudRepository<WebBoard, Integer>,
        QuerydslPredicateExecutor<WebBoard> {
    //default 키워드를 이용해서 인터페이스에서 직접 메소드의 내용을 구현해 줄 수 있습니다.
    //검색에 필요한 타입 정보와 키워드를 이용해서 적당한 쿼리를 생성합니다.
    public default Predicate makePredicate(String type, String keyword) {
        BooleanBuilder builder = new BooleanBuilder();

        QWebBoard board = QWebBoard.webBoard; // maven compile 하면 target 에 자동으로 생성됩니다
        builder.and(board.board_pk.gt(0)); // gt : 비교표현식 ('>'), 즉 게시판 번호가 0 초과

        if (type == null) {
            return builder;
        }
        switch (type) {
            case "t":
                builder.and(board.title.like("%" + keyword + "%"));
                break;
            case "c":
                builder.and(board.description.like("%" + keyword + "%"));
                break;
            case "w":
                builder.and(board.user.user_id.like("%" + keyword + "%"));
                break;
        }
        builder.and(board.board_pk.gt(0));
        return builder;
    }
}
