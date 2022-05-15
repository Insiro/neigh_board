package com.seproject;

import com.seproject.model.User;
import com.seproject.model.WebBoard;
import com.seproject.persistence.WebBoardRepository;
import lombok.extern.java.Log;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.annotation.Commit;
import org.springframework.test.context.junit4.SpringRunner;

import java.util.stream.IntStream;

@RunWith(SpringRunner.class)
@SpringBootTest
@Log
@Commit
public class WebBoardApplicationTests {
    @Autowired
    WebBoardRepository repo;

    @Test
    public void insertBoardDummies() {
        IntStream.range(0,300).forEach(i -> {

            WebBoard board = new WebBoard();
            board.setTitle("Sample Board Title " + i);
            board.setDescription("Content Sample..." + i + "of Board");
            board.setUser(new User());

            repo.save(board);

        });
    }
}
