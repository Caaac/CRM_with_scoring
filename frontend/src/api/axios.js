import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  // withCredentials: true,
  headers: {
    // 'Cookie': 'sessionid=ms385lu9zggoln6s5htadt9uhrnf00kf; csrftoken=I6KQcJGApwMj1EI2HxXKEvWKsYIGAESo'
  }
});

export { instance }