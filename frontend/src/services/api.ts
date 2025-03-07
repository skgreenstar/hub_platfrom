import axios from "axios";

const API_URL = "http://localhost:8000"; // 백엔드 API 주소

export const registerUser = async (username: string, email: string, password: string) => {
  return await axios.post(`${API_URL}/auth/register`, { username, email, password });
};

export const login = async (username: string, password: string) => {
  try {
    const response = await axios.post(`${API_URL}/auth/login`, { username, password });
    return response.data;
  } catch (error) {
    console.error("Login error:", error);
    throw error;
  }
};

export const fetchDocuments = async (query: string) => {
  try {
    const response = await axios.get(`${API_URL}/documents/search`, { params: { q: query } });
    return response.data;
  } catch (error) {
    console.error("Search error:", error);
    throw error;
  }
};



export const uploadFile = async (file: File) => {
  const formData = new FormData();
  formData.append("file", file);
  return axios.post(`${API_URL}/files/upload`, formData);
};

export const downloadFile = async (filename: string) => {
  const response = await axios.get(`${API_URL}/files/download/${filename}`, {
    responseType: "blob",
  });

  const url = window.URL.createObjectURL(new Blob([response.data]));
  const link = document.createElement("a");
  link.href = url;
  link.setAttribute("download", filename);
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
};


// 📂 파일 목록 가져오기
export const fetchFiles = async () => {
  const response = await axios.get(`${API_URL}/files/list`);
  return response.data;
};
