import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Home from "./pages/Home";
import SearchList from "./pages/SearchList";

// ✅ 로그인 여부를 확인하는 함수
const isAuthenticated = () => {
  return localStorage.getItem("token") !== null;
};

// ✅ 인증된 사용자만 접근할 수 있도록 보호
const PrivateRoute = ({ element }: { element: JSX.Element }) => {
  return isAuthenticated() ? element : <Navigate to="/" />;
};

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/register" element={<Register />} />  {/* ✅ 회원가입 페이지는 보호하지 않음 */}
        <Route path="/home" element={<PrivateRoute element={<Home />} />} />
        <Route path="/search" element={<PrivateRoute element={<SearchList />} />} />
      </Routes>
    </Router>
  );
};

export default App;
