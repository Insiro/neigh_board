import { MarkedOptions, marked } from "marked";

export const markedOption: MarkedOptions = {
  renderer: new marked.Renderer(),
  gfm: true,
  headerIds: false,
  breaks: true,
  pedantic: false,
  sanitize: true,
  smartLists: true,
  smartypants: false,
};

export const primaryColor = "#416389";
export const apiUrl = "http://neighboard.insiro.me/api";
