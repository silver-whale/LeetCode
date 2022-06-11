package Java;

public class Leetcode557 {
    public String reverseWords(String s) {
        // 공백 단위로 쪼개서 배열화
        String[] words = s.split(" ");

        // StringBuilder 객체 생성
        StringBuilder temp = new StringBuilder();

        // 각 단어마다
        for (int i = 0; i < words.length; i++) {
            // 1. String을 StringBuilder화해서 뒤집는다. 이후 공백 추가.
            // 2. 해당 StringBuilder를 다시 string화 해서 추가한다.

            // Stringbuilder.append는 문자열을 매개변수로 받아서 두 번 변환해주는 것
            temp.append(String.valueOf(new StringBuilder(words[i]).reverse()+" "));
        }

        // trim 함수: 왼쪽, 오른쪽 공백 제거
        return temp.toString().trim();
    }
}
