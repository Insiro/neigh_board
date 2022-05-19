package com.seproject.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.EqualsAndHashCode;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;
import org.springframework.stereotype.Component;

import javax.persistence.*;
import java.sql.Timestamp;
import java.time.LocalDateTime;

@Entity
@Table(name = "board")
@Data
@AllArgsConstructor
@NoArgsConstructor
@EqualsAndHashCode(of = "broad_pk")
@Component
public class WebBoard {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long board_pk; // 게시판 정보를 수정 및 삭제할때 사용하기 위한 pk, 추가된 부분 int > Long
    @ManyToOne
    @JoinColumn(name = "user_id")
    private User user; // 게시글 작성자

    private LocalDateTime register_date; // 게시글이 등록된 날짜

    @Column(length = 30)
    private String title; // 게시글 제목

    @Column(length = 3000)
    private String description; // 게시글의 내용

    private int likes; //게시글의 추천 수

    @Column(length = 50)
    private String image_name; // 내용에 첨부된 이미지를 불러오는 파일 명

    private int comment_num; //게시글의 댓글 수

    @Column(length = 100)
    private String region; // 작성자의 거주 지역

    //private Long boardNum; // 추가된 부분 : 게시판 넘버

    // 추가부분
    @CreationTimestamp
    private Timestamp regdate;
    @UpdateTimestamp
    private Timestamp updatedate;
}
