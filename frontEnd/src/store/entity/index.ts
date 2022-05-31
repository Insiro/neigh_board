export interface User {
  name: string;
  id: string;
}
export interface Post {
  author: string;
  title: string;
  content: string;
  likes: number;
  region: string;
  date: string;
  id: string;
}
export interface Comment {
  author: string;
  comment: string;
  date: string;
  id: string;
}
