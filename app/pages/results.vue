<template>
  <div class="result">
    <h1>あなたは。。。</h1>
    <img src="" alt="Ramen Fortune">
    {{ score }}
    {{ algoEgo(score) }}
    {{ judgeSentence(algoEgo(score)) }}
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  computed: {
    ...mapState(['score']),
  },
  data() {
    return {
      ramenList: [
        {
          id: 1,
          name: '',
          sentence: '',
          imageUrl: '',
        },
      ],
    };
  },
  methods: {
    algoEgo(scores) {
      if ((scores['np'] > scores['cp']) && (Math.max(Object.values(scores)) == scores['np']) && (Math.min(Object.values(scores)) == Math.min([scores['cp'], scores['ac']])) && (scores['a'] >= scores['fc'] >= scores['ac'])) {
          return 1;
      } else if((Math.min([scores['np'], scores['ac']]) >= scores['a']) && (Math.max([scores['cp'], scores['fc']]) <= scores['a'])) {
          return 2;
      } else if ((Math.max([scores['np'], scores['ac']]) <= scores['a']) && (Math.min([scores['cp'], scores['fc']]) >= scores['a'])){
          return 3;
      } else if ((Math.min([scores['cp'], scores['ac']]) >= scores['np']) && (Math.max([scores['a'], scores['fc']]) <= scores['np'])){
        return 4;
      } else if (Math.min([scores['cp'], scores['a'], scores['ac']]) >=Math.max([scores['np'], scores['fc']])){
          return 5;
      } else if (Math.min([scores['np'], scores['fc']]) >=Math.max([scores['cp'], scores['a'], scores['ac']])){
          return 6;
      } else if ((scores['a'] >= Math.max([scores['np'], scores['fc']])) && (Math.min([scores['np'], scores['fc']]) >= Math.max([scores['cp'], scores['ac']]))){
        return 7;
      } else if (scores['cp'] >= scores['np'] >= scores['a'] >= scores['fc'] >= scores['ac']){
        return 8;
      } else if (scores['cp'] <= scores['np'] <= scores['a'] <= scores['fc'] <= scores['ac']){
        return 9;
      } else {
        return 10;
      }
    },
    judgeSentence(ego) {
      if (ego==6) {
        var sentence = "あなたは蘭州牛肉拉麺タイプ。楽観主義者で、見通しが明るかろうが暗かろうが、いつも楽しいムードを醸し出しています。思いやりがあって面倒見もよく、好奇心や表現力に富んでいるなどの長所がたくさんある人なのですが、ルーズで気ままという欠点もあります。仕事中にも関わらず突然「ちょっと寝てくるわ」と言い残してどっかに行ってしまう楽観的な行動や、好奇心のあまり店に置いてある煮卵を勝手に食べ始めてしまう、まるで蘭州牛肉拉麺の店員のようなあなたには注意が必要です。とりあえず心の中でブレーキを踏むことを覚えてみましょう。";
        return sentence;
      } else if (ego==7) {
        var sentence = "あなたはラ王タイプ。論理的、現実的で仕事ができますが、頭でっかちの評論家タイプといわれることもあり、論理ばかり並べて行動や責任が伴わないと評されることもあります。確かにラ王はカップラーメンの中ではおいしい方かもしれませんが、しかし所詮インスタント。インスタント界隈の中でマウントを取り、したり顔で他のカップラーメンを見下し、批評ばかりしている、そんなラ王のようなあなたは注意が必要です。普段心の中で見下してしまっている俗世間にもたまには目を向けることを覚えましょう。";
        return sentence;
      } else if (ego==8) {
        var sentence = "あなたは二郎タイプ。昔ながらの頑固親父タイプともいわれ、融通性に乏しく他人の意見を素直に聞き入れない傾向があります。入店した順に食べ終わらない客がいたり、普通盛りを食べ切れなさそうな顔をしているのに普通盛りを頼む客がいると睨みつけてしまう、まるで二郎の店員のようなあなたは注意が必要です。もう手遅れかもしれませんが、とりあえず人の意見に耳を傾け、人に優しくすることから始めましょう。";
        return sentence;
      } else if (ego==9) {
        var sentence = "あなたはにし乃タイプ。子供っぽいタイプともいわれ、素直で従順なので協調性は高いのですが、主体性や責任感に乏しい傾向があります。また、自己中心性や依存心が顔をのぞかせる場合もあります。おしゃれな店構えであるにもかかわらず、子供っぽさの象徴であるナルトを入れてしまう、自己中心的な、まるで西乃のようなあなたには注意が必要です。もう少し大人になる努力をしてみましょう。";
        return sentence;
      } else if (ego==1) {
        var sentence = "1";
        return sentence;
      } else if (ego==2) {
        var sentence = "2";
        return sentence;
      } else if (ego==3) {
          var sentence = "3";
          return sentence;
      } else if (ego==4) {
          var sentence = "4";
          return sentence;
      } else if (ego==5) {
          var sentence = "5";
          return sentence;
      } else {
        var sentence = "あなたは三好タイプ。個性が何もなく、人間的な魅力が希薄であり、人生の楽しみを見つけにくいので、人生の充実感は薄いでしょう。特筆すべきことが何もない、そんな三好のようなあなたは注意が必要です。よく分かんないけどとりあえずラウドバンドでも始めてみると尖ってくると思います。";
        return sentence;
      }
    },
  },
  beforeDestroy() {
    this.$store.commit('setInit');
  },
};
</script>

<style scoped lang="scss">
.result {
  margin: 50px;
  min-height: 90vh;
}
</style>
