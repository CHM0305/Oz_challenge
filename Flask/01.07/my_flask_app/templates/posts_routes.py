from flask import request, jsonify, render_template
from flask_smorest import Blueprint, abort


def create_posts_blueprint(mysql):
    posts_blp = Blueprint(
        'main',
        __name__,
        description="posts api",
        url_prefix="/posts",
    )
# bp = Blueprint('main',__name__, url_prefix="/")
# 객체명 = Blueprint('별칭'__name__,url_prefix="/라우팅 함수의 애네테이션??URL 앞에 기본으로 붙힐 접두어 URL")
# 디스크립터(Descriptor) = 클래스를 통해 속성 접근을 제어하기 위한 프로토콜으로, 클래스 내에 get, set, delete 메소드를 구현함.
    
    
    #@@@라우팅(routing)기법 / 객체이름.route(/route경로이름/원하는 값)

    #posts_blp 경로에 "/"뒤에 methods 중 하나를 넣으면 아래 코드가 실행된다. 
    @posts_blp.route("/",methods = ["GET","POST"])
    def posts():
        cursor=mysql.connection.cursor()
        # GET 게시글 조회
        if request.method =="GET":
            sql = "SELECT * FROM posts"
            cursor.execute(sql)
            posts = cursor.fetchall()
            cursor.close()
            # 만약 application/json과 text/html 이 text/html에 맞다면
            if request.accept_mimetypes.best_match(['application/json', 'text/html']) == 'text/html':
                # 리스트 컴프리헨션을 사용한다. 리스트 안에 for문을!
                post_list = [{"id": post[0], "title": post[1], "content": post[2]} for post in posts]
                # render_template란, templates라는 폴더 안의 posts.html 파일을 읽어오고 posts에 리스트를 복사한다.
                return render_template("posts.html", posts=post_list)

            # JSON으로 반환
            return jsonify([{"id": post[0], "title": post[1], "content": post[2]} for post in posts])
                
        #POST 게시글 생성
        elif request.method == "POST":
            title = request.get("title")
            content = request.get("content")

            #만약 제목 또는 내용이 없다면 이라는 조건도 만들어줘야힘.
            if not title or not content:
                abort(400,message="제목 또는 내용이 없습니다. 다시 입력해주세요.")
            #조건에 알맞게 입력했다면 sql 업데이트 문으로 
            sql = "INSERT INTO posts (title, cotent) VALUES (%s, %s)"
            cursor.execute(sql,(title,content))
            mysql.connection.commit()
            #성공적으로 완료했다면 성공 메세지
            return jsonify({"message":"success"}) ,201
        


        # POST로 새 글이 생성됨의 동시에 id도 생성이 돼 메소드 뒤에 id 값을 넣어주면 함수가 실행된다!

    @posts_blp.route("/<int:id>", methods=["GET", "PUT", "DELETE"])
    def post(id):        
        cursor = mysql.connection.cursor()
        #GET 특정 게시글 조회
        #민약 GET가 입력이 되었다면 특정 게시글을 찾을 수 있는 (id)값을 찾는 SELECT 문을 만들으라
        if request.method == "GET":
            sql = f'SELECT * FROM posts WHERE id={id}'
            cursor.execute(sql)
            post = cursor.fetchone()
            #변수에 담으면 나중에 sql 찾을때 용이.

            #만약에 post 값에 아무것도 없다면 경고와 리턴을
            if not post:
                abort(404, message="해당 게시글이 없습니다.")
            return {"id" : post[0], "title" : post[1],"content" : post[2]}

        #PUT 특정 게시글 수정
        elif request.method == "PUT":
            #바로 업뎃하면 안됨! 특정 id의 게시물인지 확인 후 업데이트 해야함.
            # 1. 특정 아이디의 제목과 내용 불러오기
            title=request.json.get("title")
            content=request.json.get("content")
            # 2. 특정 아이디의 제목 또는 내용이 없으면 경고 띄우기
            if not title or not content:
                abort(400,message="제목 또는 내용이 없습니다.")

            # 3. 특정 아이디의 글과 내용을 찾아삼만리
            sql = "SELECT * FROM posts WHERE id=%s"
            cursor.execute(sql, (id,))
            post = cursor.fetchone()

            # 만약 post에 아무것도 없다면 경고
            if not post:
                abort(400,message="해당 게시글이 없습니다.")

            # 4. 조건을 통과했다면 sql문 업뎃
            sql = "UPDATE posts SET title=%s, content=%s WHERE id=%s"
            cursor.execute(sql,(title, content, id))
            mysql.connection.commit()

            return jsonify({"message": "Successfully updated title & content"})
            
        #DELETE 특정 게시글 삭제
        elif request.method == "DELETE":
            title=request.json.get("title")
            content=request.json.get("content")
            if not title or not content:
                abort(400,message="제목 또는 내용이 없습니다.")

            sql = "SELECT * FROM posts WHERE id=%s"
            cursor.execute(sql, (id,))
            post = cursor.fetchone()

            if not post:
                abort(400,message="해당 게시글이 없습니다.")

            sql = "DELETE FROM posts WHERE id=%s"
            cursor.execute(sql, (id,))
            mysql.connection.commit()

            return jsonify({"message": "Successfully deleted post"})
        
    return posts_blp
