import axios from "axios";

const instance = axios.create({
  baseURL: "https://bf36-103-92-103-2.ngrok-free.app",
});

export default instance;
