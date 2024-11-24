import axios from "axios";

const instance = axios.create({
  baseURL: "http://191.168.0.100:5000",
});

export default instance;
