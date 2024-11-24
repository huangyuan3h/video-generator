"use client";
import { invoke } from "@tauri-apps/api/core";
import { Button } from "@/components/ui/button";

export const TestButton = () => {
  const handleClick = async () => {
    const response = await invoke("greet", { name: "yuanhuang" });
    console.log(response);
  };
  return <Button onClick={handleClick}>test</Button>;
};
