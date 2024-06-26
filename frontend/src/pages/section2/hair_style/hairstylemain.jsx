import React from "react";
import styled from "styled-components";
import ClickButton from "../../../components/clickbutton";
const HairStyleContainer = styled.div`
  width: 90%;
  height: 80vh;
  margin: 60px;
  display: flex;
  justify-content: center;
  flex-direction: column;
  border-radius: 20px;
  background-color: white;
`;
const TopContainer = styled.div`
  width: 100%;
  height: 25%;
  display: flex;
  flex-direction: row;
  background-color: green;
`;
const BottomContainer = styled.div`
  width: 100%;
  height: 75%;
  background-color: beige;
`;
const BlackCircle = styled.div`
  width: 50px;
  height: 50px;
  margin: 20px 20px;
  background-color: black;
  border-radius: 50%;
`;
const TopTextContainer = styled.div`
  width: auto;
  height: 100%;
  background-color: aliceblue;
`;

const PinkText = styled.p`
  color: #e547ff;
  font-size: 5rem;
  font-weight: 700;
`;
const HairStyleMain = () => {
  return (
    <HairStyleContainer>
      <TopContainer>
        <BlackCircle />
        <TopTextContainer>
          <PinkText>Personal Color</PinkText>
        </TopTextContainer>
      </TopContainer>
      <BottomContainer>
        <ClickButton />
      </BottomContainer>
    </HairStyleContainer>
  );
};
export default HairStyleMain;
