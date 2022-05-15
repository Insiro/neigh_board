package com.seproject.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.stereotype.Component;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Data
@AllArgsConstructor
@NoArgsConstructor
@Table(name="comment")
@Component
public class Comment {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	@ManyToOne
	@JoinColumn(name="user_id")// user_id 외래키
	private User user;
	@ManyToOne
	@JoinColumn(name="board_pk")// 게시글 pk 외래키
	private WebBoard webBoard;
	
	@Column(length = 200)
	private String comment; //댓글 내용
	
	private LocalDateTime register_date;// 댓글 단 날짜
	
}
