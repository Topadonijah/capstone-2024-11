import React from "react";
import styled from "styled-components";
import About from "../../../assets/AboutText.svg";
import Girl from "../../../assets/Frame3.png";
import Slider from "../../../components/flowingCircle";
// 이미지와 대략적인 설명
const IntroduceFirst = () => {
  return (
    <MainContainer>
      <Slider />
      <SmallBlackCircle />
      <AboutText src={About}></AboutText>
      <BlackCircle>
        <Text>
          우리 서비스는 개인 맞춤형 헤어스타일과 퍼스널 컬러를 찾는 것을 도와드려요. 전문가의 도움 없이도 손쉽게 원하는
          스타일을 찾을 수 있어요. 컴퓨터비전과 인공지능 기술을 활용하여 빠르고 정확하게 사용자에게 어울리는 스타일을
          추천해 드려요. 그래서 많은 비용과 시간을 들이지 않아도 만족스러운 결과를 얻을 수 있어요
        </Text>
      </BlackCircle>
      <Girlimg src={Girl}></Girlimg>
    </MainContainer>
  );
};
const MainContainer = styled.div`
  width: 100%;
  height: 150vh;
  position: relative;
  display: flex;
`;
const Girlimg = styled.img`
  position: absolute;
  top: 20%;
  left: 20%;
`;
const AboutText = styled.img`
  position: absolute;
  bottom: 47%;
  right: 25%;
  z-index: 3;
`;
const SmallBlackCircle = styled.div`
  width: 15rem;
  height: 15rem;
  position: absolute;
  border-radius: 100%;
  top: 12%;
  left: 12%;

  background-color: black;
  z-index: 3;
`;
const BlackCircle = styled.div`
  width: 35rem;
  height: 35rem;
  position: absolute;
  border-radius: 100%;
  bottom: 5%;
  right: 25%;
  z-index: 3;
  background-color: black;
  display: flex;
  padding: 1rem 1rem 1rem 1rem;
  justify-content: center;
  align-items: center;
`;
const Text = styled.p`
  color: white;
  font-size: 1.3rem;
  text-align: center;
`;
export default IntroduceFirst;
