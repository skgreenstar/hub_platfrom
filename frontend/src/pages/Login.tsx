import React, { useState } from "react";
import { Container, TextField, Button, Typography, Box } from "@mui/material";
import { login } from "../services/api";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const data = await login(username, password);
      localStorage.setItem("token", data.access_token);
      navigate("/home"); // 로그인 성공 시 홈으로 이동
    } catch (error) {
      alert("로그인 실패");
    }
  };

  return (
    <Container maxWidth="xs">
      <Box sx={{ display: "flex", flexDirection: "column", mt: 10 }}>
        <Typography variant="h5" textAlign="center">로그인</Typography>
        <TextField label="아이디" variant="outlined" margin="normal" fullWidth value={username} onChange={(e) => setUsername(e.target.value)} />
        <TextField label="비밀번호" type="password" variant="outlined" margin="normal" fullWidth value={password} onChange={(e) => setPassword(e.target.value)} />
        <Button variant="contained" color="primary" fullWidth onClick={handleLogin}>로그인</Button>
      </Box>
    </Container>
  );
};

export default Login;
