class Solution {
    public int solution(int chicken) {
        int answer = 0;
        while (chicken >= 10) {
            answer++;
            chicken -= 9;
        }
        return answer;
    }
}