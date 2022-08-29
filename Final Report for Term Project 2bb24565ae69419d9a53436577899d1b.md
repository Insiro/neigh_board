# Final Report for Term Project

<aside>
💡

</aside>

---

# 1. Introduction

## 1.1 Motivation

Communicating freely and exchanging information about a particular field is always possible through the application. Therefore, we can communicate with people in the same field, so we can communicate well.

![Untitled](Final%20Report%20for%20Term%20Project%202bb24565ae69419d9a53436577899d1b/Untitled.png)

In fact, the popularity of service platforms centered on the neighborhood is hot recently. The biggest factor is that the prolonged social distancing has increased consumption around the house and attracted attention to the community in the residential area. Accordingly, TDI, a big data company, analyzed the current status of neighborhood-based services, focusing on local-based platforms such as 'Carrot Market' and 'Consumer Meeting'

As a result of analyzing the current status of regional-based platforms from January to May this year, the number of installers increased in 2, 3, 4, and May compared to January in both carrot markets and small groups. Carrot Market, a second-hand goods trading app, showed a steady increase of 4.7 percent in February, 7.7 percent in March, 10.7 percent in April and 14.2 percent in May. Consumption of regional-based hobby-sharing apps rose 4.3% in May, achieving a modest rise. Because it is a highly reliable app because it is a system that maintains subscription only when one certifies one's area from time to time, it is a big reason for the rise.

Distancing has become a routine, but people still want to relate and communicate with someone. It is analyzed that people's desire for connection was expressed in the neighborhood as there were restrictions on long-distance travel, and it also affected the growth rate of the installation of regional-based community platforms.

![Untitled](Final%20Report%20for%20Term%20Project%202bb24565ae69419d9a53436577899d1b/Untitled%201.png)

As a hobby sharing platform, users can participate in various gatherings by region and interest. Among app users, the gender ratio gap was not large, with 59% for men and 41% for women.

It is estimated that the main users of the app are those in their 20s and 30s. Those in their 20s and 30s accounted for the highest share of 50% and 40%, which is analyzed that job seekers and office workers who are tired of their daily lives enjoy various experiences such as sports, volunteer work, and prop production using their leisure time. In addition, the app can raise the level of language, jobs, and hobbies with "Class," a paid meeting when paying, leading the participation of 2030s who are interested in self-development

## 1.2 Scope of the system

Project scope is a means of clarifying the boundaries of a project and accurately defining objectives, deadlines, and project deliverables. Clarifying the scope of a project can help you achieve your project goals and objectives without delaying or overworking your work.

- What is the reason for this project? What are the ultimate goals and outcomes?
    - Create a platform where you can share your interests and recent issues and interact with people in the same neighborhood, similar age, and similar consensus. Based on the characteristics of the SNS app that can be easily used in everyday life and has a high frequency of admission, it is possible to provide a communication space such as sharing the same interests around the neighborhood and sharing leisure life.
- LIMITATION
    - avaliable budget ; none
    - # of people ; **4 students at Gachon University working at least 10 hours a week for 5 weeks**
    - Resource :
        1. Memory usage under 2g
        2. Storage usage under 20g
        3. Network Bandwith under 8mbps
- Project RoadMap & Timeline :
    
    ![Untitled](Final%20Report%20for%20Term%20Project%202bb24565ae69419d9a53436577899d1b/Untitled%202.png)
    
    - ~ **5/7** **:** **Specifying the scope of home page production** & Show Front-end
        
        → ERD, Make Outline, Build Server
        
    - ~ 5/14:  **Create Main API** & Development Testing
        
        → Write Board and Comment
        
    - ~ 5/21: **Create Main API** 2 & Development Testing
        
        → Filtering by Region
        
    - ~ 5/28: **Create Main API** 3 & Development Testing
        
        → Board Searching & Making Friend
        
    - ~ **6/4:**  **Actual operation of the homepage** & User Test

## 1.3 Objective and success criteria of the project

| Success Criteria | C1 :  Meeting project’s performance objective | Meets TimeLine, Ultimate Goal(above)   |
| --- | --- | --- |
|  | C2 : Meeting project’s specified objectives  | Depending on project scope |
|  | C3 : Meeting project’s requirements | All units are going to be tested |
|  | C4 : Stakeholder’s satisfaction | Satisfaction of project owner, user, project team, contractors, sponsers |
| Success Factors | F1 : Project management processes | Check structure which are following Architectural pattern& desing,  checkn planning with timeStone.  competences with Testing Tools(ex, pylint, static testing, postman etc) |
|  | F2 : Project resources | Server has limited resource so that checking resource when debugging. Check Timing( Final Presentation : 6/7) |
|  | F3 : Project team | To get Competences & skills learn more by own. commitment by using Conventional commit |
|  | F4 : Organisational culture | Communication, support, knowledge management with KanbanBoard at least every update. |
|  | F5 : Communication & cooperation | Communication among stakeholders (whose consist of persona customer) |

## 1.4 Technical skill

; **basic ability to perform tasks**

- Java : Itermediate(2), Novice(2)
- Python : Novice (4)
- Spring : N/A(4)
- Django : N/A(3), Intermediate(1)

p.s   Expert- Experienced -Intermediate-Novice-N/A 

# 2. Proposed system

## 2.1 Overview _ NEIGHBOARD

There are times when we find valuable information that is not connected in the neighborhood, and we need each other's information to solve the inconvenience in our community life. To this end, we organized the project with the aim of activating services based on empathy for local communities and neighbors. Thus, the browser NEIGHBOARD was created by combining the advantage of being able to focus users' interests based on the region and the real-time nature of communication on existing SNS. That’s why we named NEIGHBOARD, neighbor + Board.

## 2.2 Requirements analysis

- User Requirements
    - Functional Requirements
        1. User Info
        2. Login, Log out, Register
        3. Authorized in Region
        4. Post Create Reading
        Update Delete
        5. Search Post
        6. Create Comment
    - NonFuntional Requirements
        
        I. **Security** ; If there is not User information, should not
        create and delete post.
        
        II. **Safety**; Server cannot reach for User password.
        
        III. **Reliability** ; Server continually connects, if it disconnects, refactoring as soon as possible.
        
        IV. **Availability** ; Every Day, Every Hour be able to provide Service.
        
        V. **Performance (Resource Handling)** ; When User want to approach in URL, the server should show to response time under1 second.
        
- System Requirements
    - Functional Requirements
        1. Web Based ‘Board’ Software
        2. Post Board, Article CRUD
        3. Register, Login, Log out
        4. Post in considered ‘Region’
        5. Comment CRUD
        6. Alarm
    - Nonfuntional Requirements
        1. Product Requirements
            1.  Efficiency
            I. Memory Usage Under 2g
            II. Storage Usage Under 20g
            III. Network Bandwith under 8
            2.  Usability : Menu Complexity Lebel Under 6
            3. Portability : Page usable on Chrome, firefox, edge
        2. Organizational requirements
            1. Implement : JAVA Spring, MVP pattern (If it not work, then Django)
            2. Standard : Conventional Commit, IDE
        3.  External requirements
            1. Password certificate
            2. Phone number certificat

## 2.3 System modeling

![Untitled](Final%20Report%20for%20Term%20Project%202bb24565ae69419d9a53436577899d1b/Untitled%203.png)

### API Document

- **Project : User**
    
    → What does your API do?
    
    - Overview ; Things that the developers should know about
    - Authentication ; What is the preferred way of using the API?
    - Error Codes ; What errors and status codes can a user expect?
    - Rate Limit ; Is there a limit to the number of requests a user can send?
        - End-point : Board List
        
        ### Method: GET
        
        > http://{{host}}/user/test
        > 
        
        ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
        
- **Project : Post**
    
    → For Manage  post
    
    - Rate Limit
        
        ## End-point: Board List
        
        ### Method: GET
        
        > http://{{host}}/post
        > 
        
        ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
        
        ## End-point: new biard
        
        ### Method: POST
        
        > http://{{host}}/post
        > 
        
        ### Body (**raw**)
        
        ```
        {
            "title":"test_post1",
            "content":"test_content"
        }
        
        ```
        
        ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
        
        ## End-point: getPost
        
        ### Method: GET
        
        > http://{{host}}/post/{{postId}}
        > 
        
        ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
        
        ## End-point: del post
        
        ### Method: DELETE
        
        > http://{{host}}/post/{{postId}}
        > 
        
        ### Body (**raw**)
        
        ```
        {
            "pwd":"test"
        }
        
        ```
        
    
- **Project : auth**
    
    → Manage Auth
    
    - Overview
        
        pass the parms by json raw
        
    - Authentication
        
        What is the preferred way of using the API?
        
    - Rate limit
    
    ## End-point: register
    
    ### Method: POST
    
    > http://{{host}}/register
    > 
    
    ### Body formdata
    
    |  | Value | Type |
    | --- | --- | --- |
    | id | test | text |
    | pwd | test | text |
    | phone | test | text |
    | region | test | text |
    | user_name | test | text |
    
    ### Query Params
    
    |  | Value |
    | --- | --- |
    | id | test |
    | pwd | test |
    | phone | test_phone |
    | region | test_region |
    | user_name | test |
    
    ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
    
    ## End-point: is_signed
    
    ### Method: GET
    
    > http://{{host}}/auth
    > 
    
    ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
    
    ## End-point: sign
    
    ### Method: POST
    
    > http://{{host}}/auth
    > 
    
    ### Body formdata
    
    | pwd | test | text |
    | --- | --- | --- |
    | id | test | text |
    
    ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
    
    ## End-point: signOut
    
    ### Method: DELETE
    
    > http://{{host}}/auth
    > 
    
    ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
    
- **Project : comment**
    
    → manage Comment
    
    - Rate Limit
    
    ## End-point: addComment
    
    ### Method: POST
    
    > http://{{host}}/post/{{postId}}/comment
    > 
    
    ### Body (**raw**)
    
    ```
    {
        "comment": "test1"
    }
    
    ```
    
    ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
    
    ## End-point: Comment list
    
    ### Method: GET
    
    > http://{{host}}/post/{{postId}}/comment
    > 
    
    ### Body (**raw**)
    
    ```
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
    
    > http://{{host}}/comment/{{CommentId}}
    > 
    
    ### Body (**raw**)
    
    ```
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
    

## 2.4 Architectural design

![Untitled](Final%20Report%20for%20Term%20Project%202bb24565ae69419d9a53436577899d1b/Untitled%204.png)

### Architecture pattern

![Untitled](Final%20Report%20for%20Term%20Project%202bb24565ae69419d9a53436577899d1b/Untitled%205.png)

![Untitled](Final%20Report%20for%20Term%20Project%202bb24565ae69419d9a53436577899d1b/Untitled%206.png)

# 3. Validation

## 3.1 Memory Usage

![동접자 테스트 메모리 점유율.png](Final%20Report%20for%20Term%20Project%202bb24565ae69419d9a53436577899d1b/%EB%8F%99%EC%A0%91%EC%9E%90_%ED%85%8C%EC%8A%A4%ED%8A%B8_%EB%A9%94%EB%AA%A8%EB%A6%AC_%EC%A0%90%EC%9C%A0%EC%9C%A8.png)

## 3.2 Server State

![테스트중 서버 상태.png](Final%20Report%20for%20Term%20Project%202bb24565ae69419d9a53436577899d1b/%ED%85%8C%EC%8A%A4%ED%8A%B8%EC%A4%91_%EC%84%9C%EB%B2%84_%EC%83%81%ED%83%9C.png)

## 3.3 Request & Response Time

Using PostMan

![총 5264회 요청 post, login.png](Final%20Report%20for%20Term%20Project%202bb24565ae69419d9a53436577899d1b/%EC%B4%9D_5264%ED%9A%8C_%EC%9A%94%EC%B2%AD_post_login.png)

## 3.4 Portability

![portability.png](Final%20Report%20for%20Term%20Project%202bb24565ae69419d9a53436577899d1b/portability.png)

## 3.5 User Test

- Login & Register
    
    ![login Register.png](Final%20Report%20for%20Term%20Project%202bb24565ae69419d9a53436577899d1b/login_Register.png)
    
- User Page
    
    ![User page.png](Final%20Report%20for%20Term%20Project%202bb24565ae69419d9a53436577899d1b/User_page.png)
    
- Board CRUD
    
    ![display1.png](Final%20Report%20for%20Term%20Project%202bb24565ae69419d9a53436577899d1b/display1.png)
    
    ![board1.png](Final%20Report%20for%20Term%20Project%202bb24565ae69419d9a53436577899d1b/board1.png)
    
- Comment CRUD
    
    ![comment.png](Final%20Report%20for%20Term%20Project%202bb24565ae69419d9a53436577899d1b/comment.png)
    
    ![comment2.png](Final%20Report%20for%20Term%20Project%202bb24565ae69419d9a53436577899d1b/comment2.png)
    

# 4. Glossary & Open Source

This notice was created using Kakao's OLIVE Platform. Use this notice for reference purposes only. Kakao does not guarantee the reliability or accuracy of the notice. All responsibilities arising from the use of OLIVE Platform and the notice rest entirely with users, and Kakao assumes no responsibility for any user or third party.

## 4.1 OSS Notice | neigh_board

This application is Copyright © (owner name). All rights reserved.

The following sets forth attribution notices for third party software that may be contained in this application.

- **@vue/eslint-config-prettier**
    
    [https://github.com/vuejs/eslint-config-prettier](https://github.com/vuejs/eslint-config-prettier)
    
    Copyright 2018-present Evan You
    
    MIT License
    
- **axios**
    
    [https://github.com/axios/axios](https://github.com/axios/axios)
    
    Copyright 2014-present Matt Zabriskie
    
    MIT License
    
- **Bootstrap**
    
    [https://github.com/twbs/bootstrap/](https://github.com/twbs/bootstrap/)
    
    Copyright 2011-2017 Twitter, Inc.
    
    Copyright 2011-2017 The Bootstrap Authors
    
    MIT License
    
- **bootstrap-vue-3**
    
    [https://github.com/cdmoro/bootstrap-vue-3](https://github.com/cdmoro/bootstrap-vue-3)
    
    MIT License
    
- **DefinitelyTyped**
    
    [https://github.com/DefinitelyTyped/DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped)
    
    Copyright property of respective owners
    
    MIT License
    
- **Delightful JavaScript Testing**
    
    [https://github.com/facebook/jest](https://github.com/facebook/jest)
    
    Copyright Facebook, Inc. and its affiliates.
    
    MIT License
    
- **dotenv**
    
    [https://github.com/bkeepers/dotenv](https://github.com/bkeepers/dotenv)
    
    Copyright 2012 Brandon Keepers
    
    MIT License
    
- **ESLint**
    
    [https://github.com/eslint/eslint](https://github.com/eslint/eslint)
    
    Copyright JS Foundation and other contributors, [https://js.foundation](https://js.foundation/)
    
    MIT License
    
- **eslint-config-prettier**
    
    [https://github.com/prettier/eslint-config-prettier](https://github.com/prettier/eslint-config-prettier)
    
    Copyright 2017, 2018, 2019 Simon Lydell and contributors
    
    MIT License
    
- **eslint-plugin-prettier**
    
    [https://github.com/prettier/eslint-plugin-prettier](https://github.com/prettier/eslint-plugin-prettier)
    
    Copyright 2017 Andres Suarez and Teddy Katz
    
    MIT License
    
- **eslint-plugin-vue**
    
    [https://github.com/vuejs/eslint-plugin-vue](https://github.com/vuejs/eslint-plugin-vue)
    
    Copyright 2017 Toru Nagashima
    
    MIT License
    
- **jinder path**
    
    [https://github.com/jinder/path](https://github.com/jinder/path)
    
    Copyright Joyent, Inc. and other Node contributor.
    
    MIT License
    
- **Marked**
    
    [https://github.com/markedjs/marked](https://github.com/markedjs/marked)
    
    Copyright 2011-2018, Christopher Jeffrey
    
    MIT License
    
- **normalize.css**
    
    [https://github.com/necolas/normalize.css](https://github.com/necolas/normalize.css)
    
    Copyright Nicolas Gallagher and Jonathan Neal
    
    MIT License
    
- **Prettier**
    
    [https://github.com/prettier/prettier](https://github.com/prettier/prettier)
    
    Copyright James Long and contributors
    
    MIT License
    
- **serve**
    
    [https://github.com/zeit/serve](https://github.com/zeit/serve)
    
    Copyright 2018 ZEIT, Inc.
    
    MIT License
    
- **TypeScript**
    
    [https://github.com/Microsoft/TypeScript](https://github.com/Microsoft/TypeScript)
    
    Copyright 2012-2020 Microsoft
    
    Apache License 2.0
    
- **TypeScript ESLint**
    
    [https://github.com/typescript-eslint/typescript-eslint](https://github.com/typescript-eslint/typescript-eslint)
    
    Copyright JS Foundation and other contributors, [https://js.foundation](https://js.foundation/)
    
    BSD 2-Clause "Simplified" License
    
- **Vite**
    
    [https://github.com/vitejs/vite](https://github.com/vitejs/vite)
    
    Copyright 2019-present, Yuxi (Evan) You and Vite contributors
    
    MIT License
    
- **vite-plugin-eslint**
    
    [https://github.com/gxmari007/vite-plugin-eslint](https://github.com/gxmari007/vite-plugin-eslint)
    
    Copyright Xiang Gao
    
    MIT License
    
- **Vue Class Component**
    
    [https://github.com/vuejs/vue-class-component](https://github.com/vuejs/vue-class-component)
    
    Copyright 2015-present Evan You
    
    MIT License
    
- **Vue CLI**
    
    [https://github.com/vuejs/vue-cli](https://github.com/vuejs/vue-cli)
    
    Copyright 2017-present, Yuxi (Evan) You
    
    MIT License
    
- **vue-eslint-parser**
    
    [https://github.com/vuejs/vue-eslint-parser](https://github.com/vuejs/vue-eslint-parser)
    
    Copyright Toru Nagashima
    
    MIT License
    
- **vue-jest**
    
    [https://github.com/vuejs/vue-jest](https://github.com/vuejs/vue-jest)
    
    Copyright Edd Yerburgh
    
    MIT License
    
- **vue-router**
    
    [https://github.com/vuejs/vue-router](https://github.com/vuejs/vue-router)
    
    Copyright 2013-present Evan You
    
    MIT License
    
- **vue-tsc**
    
    [https://github.com/johnsoncodehk/volar](https://github.com/johnsoncodehk/volar)
    
    MIT License
    
- **Vue.js**
    
    [https://github.com/vuejs/vue](https://github.com/vuejs/vue)
    
    Copyright 2013-present, Yuxi (Evan) You
    
    MIT License
    
- **Vuex**
    
    [https://github.com/vuejs/vuex](https://github.com/vuejs/vuex)
    
    Copyright 2015-present Evan You
    
    MIT License
    
- **vuex-module-decorators**
    
    [https://github.com/championswimmer/vuex-module-decorators](https://github.com/championswimmer/vuex-module-decorators)
    
    Copyright 2018 Arnav Gupta
    
    MIT License
    

## 4.2 Apache License 2.0

```
Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.

"License" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document.

"Licensor" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License.

"Legal Entity" shall mean the union of the acting entity and all other entities that control, are controlled by, or are under common control with that entity. For the purposes of this definition, "control" means (i) the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the outstanding shares, or (iii) beneficial ownership of such entity.

"You" (or "Your") shall mean an individual or Legal Entity exercising permissions granted by this License.

"Source" form shall mean the preferred form for making modifications, including but not limited to software source code, documentation source, and configuration files.

"Object" form shall mean any form resulting from mechanical transformation or translation of a Source form, including but not limited to compiled object code, generated documentation, and conversions to other media types.

"Work" shall mean the work of authorship, whether in Source or Object form, made available under the License, as indicated by a copyright notice that is included in or attached to the work (an example is provided in the Appendix below).

"Derivative Works" shall mean any work, whether in Source or Object form, that is based on (or derived from) the Work and for which the editorial revisions, annotations, elaborations, or other modifications represent, as a whole, an original work of authorship. For the purposes of this License, Derivative Works shall not include works that remain separable from, or merely link (or bind by name) to the interfaces of, the Work and Derivative Works thereof.

"Contribution" shall mean any work of authorship, including the original version of the Work and any modifications or additions to that Work or Derivative Works thereof, that is intentionally submitted to Licensor for inclusion in the Work by the copyright owner or by an individual or Legal Entity authorized to submit on behalf of the copyright owner. For the purposes of this definition, "submitted" means any form of electronic, verbal, or written communication sent to the Licensor or its representatives, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, the Licensor for the purpose of discussing and improving the Work, but excluding communication that is conspicuously marked or otherwise designated in writing by the copyright owner as "Not a Contribution."

"Contributor" shall mean Licensor and any individual or Legal Entity on behalf of whom a Contribution has been received by Licensor and subsequently incorporated within the Work.

2. Grant of Copyright License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form.

3. Grant of Patent License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work, where such license applies only to those patent claims licensable by such Contributor that are necessarily infringed by their Contribution(s) alone or by combination of their Contribution(s) with the Work to which such Contribution(s) was submitted. If You institute patent litigation against any entity (including a cross-claim or counterclaim in a lawsuit) alleging that the Work or a Contribution incorporated within the Work constitutes direct or contributory patent infringement, then any patent licenses granted to You under this License for that Work shall terminate as of the date such litigation is filed.

4. Redistribution. You may reproduce and distribute copies of the Work or Derivative Works thereof in any medium, with or without modifications, and in Source or Object form, provided that You meet the following conditions:

     (a) You must give any other recipients of the Work or Derivative Works a copy of this License; and

     (b) You must cause any modified files to carry prominent notices stating that You changed the files; and

     (c) You must retain, in the Source form of any Derivative Works that You distribute, all copyright, patent, trademark, and attribution notices from the Source form of the Work, excluding those notices that do not pertain to any part of the Derivative Works; and

     (d) If the Work includes a "NOTICE" text file as part of its distribution, then any Derivative Works that You distribute must include a readable copy of the attribution notices contained within such NOTICE file, excluding those notices that do not pertain to any part of the Derivative Works, in at least one of the following places: within a NOTICE text file distributed as part of the Derivative Works; within the Source form or documentation, if provided along with the Derivative Works; or, within a display generated by the Derivative Works, if and wherever such third-party notices normally appear. The contents of the NOTICE file are for informational purposes only and do not modify the License. You may add Your own attribution notices within Derivative Works that You distribute, alongside or as an addendum to the NOTICE text from the Work, provided that such additional attribution notices cannot be construed as modifying the License.

     You may add Your own copyright statement to Your modifications and may provide additional or different license terms and conditions for use, reproduction, or distribution of Your modifications, or for any such Derivative Works as a whole, provided Your use, reproduction, and distribution of the Work otherwise complies with the conditions stated in this License.

5. Submission of Contributions. Unless You explicitly state otherwise, any Contribution intentionally submitted for inclusion in the Work by You to the Licensor shall be under the terms and conditions of this License, without any additional terms or conditions. Notwithstanding the above, nothing herein shall supersede or modify the terms of any separate license agreement you may have executed with Licensor regarding such Contributions.

6. Trademarks. This License does not grant permission to use the trade names, trademarks, service marks, or product names of the Licensor, except as required for reasonable and customary use in describing the origin of the Work and reproducing the content of the NOTICE file.

7. Disclaimer of Warranty. Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.

8. Limitation of Liability. In no event and under no legal theory, whether in tort (including negligence), contract, or otherwise, unless required by applicable law (such as deliberate and grossly negligent acts) or agreed to in writing, shall any Contributor be liable to You for damages, including any direct, indirect, special, incidental, or consequential damages of any character arising as a result of this License or out of the use or inability to use the Work (including but not limited to damages for loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses), even if such Contributor has been advised of the possibility of such damages.

9. Accepting Warranty or Additional Liability. While redistributing the Work or Derivative Works thereof, You may choose to offer, and charge a fee for, acceptance of support, warranty, indemnity, or other liability obligations and/or rights consistent with this License. However, in accepting such obligations, You may act only on Your own behalf and on Your sole responsibility, not on behalf of any other Contributor, and only if You agree to indemnify, defend, and hold each Contributor harmless for any liability incurred by, or claims asserted against, such Contributor by reason of your accepting any such warranty or additional liability.

END OF TERMS AND CONDITIONS

APPENDIX: How to apply the Apache License to your work.

To apply the Apache License to your work, attach the following boilerplate notice, with the fields enclosed by brackets "[]" replaced with your own identifying information. (Don't include the brackets!)  The text should be enclosed in the appropriate comment syntax for the file format. We also recommend that a file or class name and description of purpose be included on the same "printed page" as the copyright notice for easier identification within third-party archives.

Copyright [yyyy] [name of copyright owner]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

```

## 4.3 BSD 2-Clause "Simplified" License

```
Copyright (c)   . All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

   1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

```

## 4.4 MIT License

```
MIT License

Copyright (c)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INC
```

# 5. Review

## 5.1 Schedule by Kanban Board

[Schedule · Insiro/neigh_board](https://github.com/Insiro/neigh_board/projects/1)

## 5.2 Role & Contribution

[Role & Contribution](https://www.notion.so/59103da4c1e942cd870ac047d635d63a)

## 5.3 Realization

### 5.3.1 Gihyun Kim

Before this project, when I was junior in college, There were two things that I didn’t know.

First, I didn’t know how the Software System is launched and what the Software processes are.

Second, I didn’t know how the web server is controlled and how the page is updated in User Environment. 

In this project, since I learned the lecture of ‘Software Engineering’, I was able to know the process of the software system from specifying requirements to evolution. Also I could know how the Web Page is controlled in Server and the Response, Request process of HTTP using ‘django, Spring Framework’. 

Now then, I will study the domain service and the useful performance of web page.

### 5.3.2 Sunghoon Kim

I made various own rules and developed them accordingly.

I was able to develop it in compliance with conventional commit, coding convention, and git flow that I had never done before.

Although tools helped to comply with convention, there were limitations and difficulties.

It was also my first time to create a document. Although API documents such as swagger were written through postman, there were difficulties in many places because there was no experience in writing them.

The same was true of system testing. Various tests such as load test and flooding test were performed. It was difficult to write the correct test while doing each test.

It was a great opportunity to experience and learn the whole process from design to testing.

### 5.3.3 Doyeon Hyun

As the project was created following the end-to-end process, it was a project that I started with the hope that it would be a time to deal with Back-end, which I usually did not encounter well. 

I wondered if it was a useless challenge because I had to acquire and utilize a lot of information within a month, but I think it was a useful time because I learned a lot of new things such as mvp pattern(Model-View-Presenter), pipenv(virtual environment), and postman(API testing tool). 

It was a project that was able to realize the importance and necessity of each step by following the clear guidelines of the steps that had been vaguely thought of while carrying out the project before.