const clientId = "ec5864d80bcf61d0ca7279c89a3affc8";
const SecretKey =
  "ec5864d80bcf61d0ca7279c89a3affc81bc649d6d994674369ed487439494c2867df09b7";
const callbackURL = "https://plasmacodeing.tistory.com/";

let urls = `https://www.tistory.com/oauth/authorize?client_id=${clientId}&redirect_uri=${callbackURL}&response_type=token`;
result = window.open(urls);
access_token = location.hash.match(/(?<=\#access_token=)[\w\W]+(?=&)/);
console.log(access_token);

let access_token =
  "e884123dd66242ecdd10905c1ccb29bc_852b1520863ca2aa02220f24533277df";

const bloginfo = `https://www.tistory.com/apis/blog/info?access_token=${access_token}&output=json`;
window.open(bloginfo);

const blogName = "plasmacodeing";
const title = "API TEST";
const content = `<h1>HELOOW !@#$!@ <span>와 이거 진짜 되나?</span></h1>`;
const visibility = 3;
const tag = "플라즈마,포토샵,인프런,치킨전쟁,API";
const blogwrite = `https://www.tistory.com/apis/post/write?access_token=${access_token}&output=json&blogName=${blogName}&title=${title}`;
//const blogwrite = `https://www.tistory.com/apis/post/write?access_token=${access_token}&output=json&blogName=${blogName}&title=${title}&content=${content}&visibility=${visibility}&tag=${tag}`;
window.open(blogwrite);

//출처: https://sub0709.tistory.com/37 [쓸데없는 코딩하기]
