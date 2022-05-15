package com.seproject.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.stereotype.Component;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Data // @ToString, @EqualsAndHashCode, @Getter, @Setter 등 자동완성
@AllArgsConstructor // 생성자 자동완성
@NoArgsConstructor // 어떠한 변수도 사용하지 않는 기본 생성자 자동 완성
@Table(name="users")
@Component
public class User {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int user_pk; // 유저 정보를 수정 및 삭제할때 사용하기 위한 pk
	
	@Column(length = 80)
	private String user_id; // 아이디
	
	@Column(length = 200)
	private String user_pw; // 비밀번호 -> 암호화를 위해 12에서 확장
	
	private LocalDateTime register_date; // 사용자가 회원가입을 한 날짜
	
	private String phone; // 휴대폰 번호
	
	@Column(length = 100)
	private String region; // 거주 지역
}
