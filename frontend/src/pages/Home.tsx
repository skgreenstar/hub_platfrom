import React from "react";
import { Container, Typography, Box } from "@mui/material";
import Navbar from "../components/Navbar";

const Home = () => {
  return (
    <>
      <Navbar />
      <Container>
        <Box sx={{ mt: 5, textAlign: "center" }}>
          <Typography variant="h4">환영합니다!</Typography>
          <Typography variant="body1">검색 기능을 사용하여 문서를 찾아보세요.</Typography>
        </Box>
      </Container>
    </>
  );
};

export default Home;
