package com.seproject.controller;

import com.seproject.model.WebBoard;
import com.seproject.persistence.WebBoardRepository;
import com.seproject.vo.PageMaker;
import com.seproject.vo.PageVO;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.data.web.PageableDefault;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import lombok.extern.java.Log;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@Controller
@RequestMapping("/boards/")
@Log
public class WebBoardController {

    @Autowired
    /**Repository 와 연동처리 부분*/
    private WebBoardRepository repo;

    @GetMapping("/list")
    public void list(@ModelAttribute("pageVO") PageVO vo, Model model) {
        Pageable page = vo.makePageable(0, "board_pk");

        //makePredicate 의 파라미터는 아직 검색조건에 대한 처리를 진행하지 않았으므로 null 입력
        //사용자가 지정하는 검색 조건과 키워드를 입력했을 때 처리가 가능하도록 검색 조건을 PageVo 와 controller 에서 만든다.
        //PageVO 에서 getType(), getKeyword()
        Page<WebBoard> result = repo.findAll(repo.makePredicate(vo.getType(), vo.getKeyword()), page);

        log.info("" + page);
        log.info("" + result);

        // model 에 page 를 직접 담는 것이 아니라 page maker 로 통해 만들어진 page 를 담는다.
        model.addAttribute("result", new PageMaker(result));
    }
    /* 다음은 비효율적인 코드입니다.
    public void list(
        //PageableDefault 를 이용하여 Pageable 타입의 객체를 만들어주어
        //페이지 처리에 파라미터를 편리하게 지정해준다
        @PageableDefault(
                direction = Sort.Direction.DESC,
                sort="board_pk",
                size=10, // 게시물의 수
                page=0) Pageable page ) {
        log.info("list() called..." + page);
    }*/

    /**
     * 게시물의 입력과 처리 부분
     * get 방식을 사용하여 입력되는 화면을 보고
     * post 방식을 사용하여 새로운 게시물을 등록하도록 처리한다.
     * RedirectAttributes는 URL 로 보이지 않아 브라우저의 주소창에서는 볼 수 없다.
     */
    @GetMapping("/register")
    public void registerGET(@ModelAttribute("vo") WebBoard vo) {
        log.info("register get");
    }

    @PostMapping("/register")
    public String registerPOST(@ModelAttribute("vo") WebBoard vo, RedirectAttributes rttr) {
        log.info("register post");
        log.info("" + vo);

        repo.save(vo);
        // redirect 를 하지 않으면 사용자가 여러번 게시물을 등록할 수 있기 때문에(post - redirect - get)방식
        rttr.addFlashAttribute("msg", "success");

        return "redirect:/boards/list";
    }

    /**
     * 게시물 조회 부분
     * 경로로 전달되는 데이터는 게시물의 번호, 검색 조건, 페이징 조건
     * 검색 조건과 페이징 조건은 PageVO 로 가능
     */
    @GetMapping("/view")
    public void view(Long board_pk, @ModelAttribute("pageVO") PageVO vo, Model model) {
        log.info("board_pk: " + board_pk);

        repo.findById(Math.toIntExact(board_pk)).ifPresent(board -> model.addAttribute("vo", board));
    }

    /**
     * 게시물의 삭제와 수정
     * 페이지의 수정 삭제는 별도의 페이지로 이동해서 처리된다.
     */
    @GetMapping("/modify")
    // boards/list/modify?=5 < modify

    public void modify(Long board_pk, @ModelAttribute("pageVO") PageVO vo, Model model) {
        log.info("MODIFY board_pk: " + board_pk);
        repo.findById(Math.toIntExact(board_pk)).ifPresent(board -> model.addAttribute("vo", board));
    }

    @PostMapping("/delete")
    //localhost:8080/boards/list/delete?=3(게시물번호 3 board_pk)
    public String delete(Long board_pk, PageVO vo, RedirectAttributes rttr) {
        log.info("DELETE board_pk: " + board_pk);

        repo.deleteById(Math.toIntExact(board_pk));
        rttr.addFlashAttribute("msg", "success");

        // 페이징과 검색했던 결과로 이동하는 경우
        rttr.addAttribute("page", vo.getPage());
        rttr.addAttribute("size", vo.getSize());
        rttr.addAttribute("type", vo.getType());
        rttr.addAttribute("keyword", vo.getKeyword());

        return "redirect:/boards/list";
    }

    @PostMapping("/modify")
    public String modifyPost(WebBoard board, PageVO vo, RedirectAttributes rttr) {
        log.info("Modify WebBoard: " + board);

        repo.findById(Math.toIntExact(board.getBoard_pk())).ifPresent(origin -> {
            origin.setTitle(board.getTitle());
            origin.setDescription(board.getDescription());

            repo.save(origin);
            rttr.addFlashAttribute("msg", "success");
            rttr.addAttribute("board_pk", origin.getBoard_pk());
        });

        rttr.addAttribute("page", vo.getPage());
        rttr.addAttribute("size", vo.getSize());
        rttr.addAttribute("type", vo.getType());
        rttr.addAttribute("keyword", vo.getKeyword());

        return "redirect:/boards/view";
    }
}
