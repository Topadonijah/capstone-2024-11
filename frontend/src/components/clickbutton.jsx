import React, { useState } from "react";
import styled from "styled-components";
import InformationModal from "./informationModal";

// React 컴포넌트
const ClickButton = () => {
  const [modalOpen, setModalOpen] = useState(false);
  const handleModalOpen = () => {
    setModalOpen(true);
  };
  const handleModalClose = () => {
    setModalOpen(false);
  };

  return (
    <Container>
      <Button onClick={handleModalOpen}>Click Me!</Button>
      {modalOpen && <InformationModal onClose={handleModalClose} />}
    </Container>
  );
};
const Container = styled.div`
  z-index: 80;
  left: 45%;
  top: 80%;
  position: absolute;
`;
// Styled Components 정의
const Button = styled.button`
  position: relative;
  display: inline-block;
  cursor: pointer;
  outline: none;
  border: 0;
  vertical-align: middle;
  text-decoration: none;
  font-size: inherit;
  font-family: inherit;
  font-weight: 600;
  color: #382b22;
  text-transform: uppercase;
  padding: 1.25em 2em;
  background: white;
  border: 2px solid #000000;
  border-radius: 0.75em;
  transform-style: preserve-3d;
  transition: transform 150ms cubic-bezier(0, 0, 0.58, 1), background 150ms cubic-bezier(0, 0, 0.58, 1);

  &::before {
    position: absolute;
    content: "";
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: #000000;
    border-radius: inherit;
    box-shadow: 0 0 0 2px #000000, 0 0.625em 0 0 white;
    transform: translate3d(0, 0.75em, -1em);
    transition: transform 150ms cubic-bezier(0, 0, 0.58, 1), box-shadow 150ms cubic-bezier(0, 0, 0.58, 1);
  }

  &:hover {
    background: #ffd166;
    transform: translate(0, 0.25em);
    &::before {
      box-shadow: 0 0 0 2px #000000, 0 0.5em 0 0 white;
      transform: translate3d(0, 0.5em, -1em);
    }
  }

  &:active {
    background: #ffd166;
    transform: translate(0em, 0.75em);
    &::before {
      box-shadow: 0 0 0 2px #b18597, 0 0 #ffe3e2;
      transform: translate3d(0, 0, -1em);
    }
  }
`;

export default ClickButton;
