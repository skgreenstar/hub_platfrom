import axios from "axios";

const API_BASE = "http://localhost:8000";

export const uploadFile = async (file: File) => {
  const formData = new FormData();
  formData.append("file", file);
  return axios.post(`${API_BASE}/files/upload`, formData);
};

export const downloadFile = async (filename: string) => {
  const response = await axios.get(`${API_BASE}/files/download/${filename}`, {
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