"use client";
import React from "react";
import styled from "styled-components";
import { FaExclamationTriangle, FaUserCircle } from "react-icons/fa";

// Tipagem das propriedades
interface CommentProps {
  usuario: string;
  data: string;
  texto: string;
  estrelas: number;
  alerta?: boolean;
}

// Estilização com styled-components
const CommentContainer = styled.div`
  display: flex;
  flex-direction: column;
  border: 1px solid #ddd;
  padding: 16px;
  border-radius: 8px;
  position: relative;
  background: #fff;
  margin-bottom: 12px;
  max-width: 500px;
`;

const Header = styled.div`
  display: flex;
  align-items: center;
  gap: 10px;
`;

const UserInfo = styled.div`
  display: flex;
  flex-direction: column;
`;

const UserName = styled.span`
  font-weight: bold;
`;

const DateText = styled.span`
  color: #888;
  font-size: 14px;
`;

const Stars = styled.div`
  display: flex;
  color: gold;
  font-size: 18px;
`;

const AlertIcon = styled(FaExclamationTriangle)`
  position: absolute;
  top: 16px;
  right: 16px;
  color: red;
  font-size: 18px;
`;

const CommentText = styled.p`
  margin-top: 8px;
  font-size: 14px;
  color: #333;
`;

// Componente principal
const Comment: React.FC<CommentProps> = ({ usuario, data, texto, estrelas, alerta }) => {
  return (
    <CommentContainer>
      <Header>
        <FaUserCircle size={32} color="#888" />
        <UserInfo>
          <UserName>{usuario}</UserName>
          <DateText>{data}</DateText>
        </UserInfo>
      </Header>

      <Stars>
        {"★".repeat(Math.max(0, Math.min(5, estrelas)))} 
        {"☆".repeat(5 - Math.max(0, Math.min(5, estrelas)))}
      </Stars>

      <CommentText>{texto}</CommentText>

      {alerta && <AlertIcon />}
    </CommentContainer>
  );
};

export default Comment;