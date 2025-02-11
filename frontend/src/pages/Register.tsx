import React, { useState } from "react";
import { Container, TextField, Button, Typography, Box } from "@mui/material";
import { registerUser } from "../services/api";
import { useNavigate } from "react-router-dom";

const Register = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const navigate = useNavigate();

  const handleRegister = async () => {
    if (password !== confirmPassword) {
      alert("비밀번호가 일치하지 않습니다.");
      return;
    }
    try {
      await registerUser(username, email, password);
      alert("회원가입 성공! 로그인 페이지로 이동합니다.");
      navigate("/");
    } catch (error) {
      alert("회원가입 실패: " + error.response.data.detail);
    }
  };

  return (
    <Container maxWidth="sm">
      <Box 
        sx={{ 
          display: "flex", 
          flexDirection: "column", 
          alignItems: "center", 
          justifyContent: "center", 
          minHeight: "100vh"
        }}
      >
        <Typography variant="h5" textAlign="center" sx={{ mb: 3 }}>
          회원 가입
        </Typography>
        <TextField label="아이디" variant="outlined" margin="normal" fullWidth value={username} onChange={(e) => setUsername(e.target.value)} />
        <TextField label="이메일" type="email" variant="outlined" margin="normal" fullWidth value={email} onChange={(e) => setEmail(e.target.value)} />
        <TextField label="비밀번호" type="password" variant="outlined" margin="normal" fullWidth value={password} onChange={(e) => setPassword(e.target.value)} />
        <TextField label="비밀번호 확인" type="password" variant="outlined" margin="normal" fullWidth value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} />
        <Button variant="contained" color="primary" fullWidth sx={{ mt: 2 }} onClick={handleRegister}>
          회원 가입
        </Button>
      </Box>
    </Container>
  );
};

export default Register;
