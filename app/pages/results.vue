<template>
  <div class="result">
    <h1>あなたのラーメンは。。。</h1>
    <div class="result__contents">
      <div
        class="result__ramenName"
        v-text="ramenList[algoEgo(score) - 1].name"
      />
      <img
        class="result__ramenImage"
        :src="ramenImgUrl(algoEgo(score))"
        alt="Ramen Fortune"
      >
      <div
        class="result__judgeSentence"
        v-html="ramenList[algoEgo(score) - 1].sentence"
      />
      <nuxt-link
        class="result__toTopPage"
        to="/"
      >
        <el-button
          type="info"
          class="result__toTopPage__button"
        >
          <i class="el-icon-caret-right" /> トップページに戻る
        </el-button>
      </nuxt-link>
    </div>
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
          name: '金子',
          sentence: 'あなたは <b>金子</b> タイプ。<br>自我状態のバランスが良い状態といえ、他人との衝突やトラブルが生じにくい型といわれています。優しく思いやりがあるので人間関係においては理想に近いタイプです。<br>日本人に多くみられるため、和を尊重する日本人らしいともいえます。ラーメンのバランスのバランスが良く、歴史があって和を尊重している、そんな金子のようなあなたはすばらしい性格をしています。これからもそのままのあなたでいて下さい。',
        },
        {
          id: 2,
          name: '日高屋 -六本木店- ',
          sentence: 'あなたは <b>六本木に店を構えてしまった日高屋</b> タイプ。<br>自分の子供に対するように、他人に対しても自分を犠牲にして献身的に尽くす優しい人です。面倒見が良く思いやりのある人ですが、自分の立場や技量を考えずに行動してしまう危うさがあるため、人に利用されたり、だまされたりしやすい型でもあります。<br>低価格を売りにしている三流店舗であるにも関わらず、立場をわきまえずに一流店舗が多く揃う六本木に店を構えてしまった日高屋のようなあなたには注意が必要です。まずは自分自身の実力を真摯に受け止めましょう。ときには諦めることも肝心です。',
        },
        {
          id: 3,
          name: '火山',
          sentence: 'あなたは <b>火山</b> タイプ。<br>高い理想と旺盛な好奇心をもち、目標を見つけては邁進していく傾向があります。時代に先駆けた組織のカリスマ的リーダーになったり、クリエイティブなものを次々と創りだす芸術家なども多いようです。何としてでものし上がろうとする野心家タイプなので、目的のためなら手段を選ばない面もあり、他人を踏み台にしたり、ワンマンな態度をとってしまうこともあります。<br>石焼ラーメンという時代を先駆けた芸術的なラーメンであったにも関わらず、そのあまりの芸術性から一般大衆に受け入れられることなく閉店に追い込まれた、そんな火山のようなあなたは注意が必要です。パフォーマンスがいくら面白くても味は変わりません。一度冷静になって何故閉店してしまったのか、考えてみましょう。',
        },
        {
          id: 4,
          name: '用心棒',
          sentence: 'あなたは <b>用心棒</b> タイプ。<br>自分にも他人にも厳しく支配的な傾向にあります。このタイプは、自分にも他人にも否定的で不満を覚えているにも関わらず、他人の評価を気にして遠慮がちになってしまうため、なかなか思っていることが言えずストレスを溜めこんでしまうことが少なくありません。二郎系ラーメンのインスパイアである自分自身にも、そしてまた二郎自体にも不満を覚えているにも関わらず、ついつい遠慮がちになってしまいストレスを溜め込んでしまっている、そんな用心棒のようなあなたには注意が必要です。<br>もやしを増やそうが、麺を太くしようが、油を増やそうが、ストレスの根本を解消しなければ不満は解消されません。一度自身のラーメン観を見つめなおしてみましょう。',
        },
        {
          id: 5,
          name: 'スシロー',
          sentence: 'あなたは <b>スシローのラーメン</b> タイプ。<br>厭世タイプと言え、時代や社会の情勢、自分の技量や立場を見抜ける観察眼を持ち、厳格で論理的な批判精神を持っていますが、自己矛盾による葛藤をいつも感じています。寿司屋であるにも関わらずラーメンを提供するという、時代や社会の情勢を見抜ける観察眼を持っていながら、その自己矛盾にいつも悩まされている、そんなスシローのラーメンのようなあなたには注意が必要です。<br>寿司屋だってラーメンを提供しても良い、そう考えるだけで自己矛盾の悩みは大分楽になると思います。そもそもシャリの上にハンバーグをのせたものを寿司として提供している時点で最早何でもありなので悩む必要はありません。',
        },
        {
          id: 6,
          name: '蘭州牛肉拉麺',
          sentence: 'あなたは <b>蘭州牛肉拉麺</b> タイプ。<br>楽観主義者で、見通しが明るかろうが暗かろうが、いつも楽しいムードを醸し出しています。思いやりがあって面倒見もよく、好奇心や表現力に富んでいるなどの長所がたくさんある人なのですが、ルーズで気ままという欠点もあります。<br>仕事中にも関わらず突然「ちょっと寝てくるわ」と言い残してどっかに行ってしまう楽観的な行動や、好奇心のあまり店に置いてある煮卵を勝手に食べ始めてしまう、まるで蘭州牛肉拉麺の店員のようなあなたには注意が必要です。とりあえず心の中でブレーキを踏むことを覚えてみましょう。',
        },
        {
          id: 7,
          name: 'ラ王',
          sentence: 'あなたは <b>ラ王</b> タイプ。<br>論理的、現実的で仕事ができますが、頭でっかちの評論家タイプといわれることもあり、論理ばかり並べて行動や責任が伴わないと評されることもあります。確かにラ王はカップラーメンの中ではおいしい方かもしれませんが、しかし所詮インスタント。インスタント界隈の中でマウントを取り、したり顔で他のカップラーメンを見下し、批評ばかりしている、そんなラ王のようなあなたは注意が必要です。<br>普段心の中で見下してしまっている俗世間にもたまには目を向けることを覚えましょう。',
        },
        {
          id: 8,
          name: '二郎',
          sentence: 'あなたは <b>二郎</b> タイプ。<br>昔ながらの頑固親父タイプともいわれ、融通性に乏しく他人の意見を素直に聞き入れない傾向があります。入店した順に食べ終わらない客がいたり、普通盛りを食べ切れなさそうな顔をしているのに普通盛りを頼む客がいると睨みつけてしまう、まるで二郎の店員のようなあなたは注意が必要です。<br>もう手遅れかもしれませんが、とりあえず人の意見に耳を傾け、人に優しくすることから始めましょう。',
        },
        {
          id: 9,
          name: 'にし乃',
          sentence: 'あなたは <b>にし乃</b> タイプ。<br>子供っぽいタイプともいわれ、素直で従順なので協調性は高いのですが、主体性や責任感に乏しい傾向があります。また、自己中心性や依存心が顔をのぞかせる場合もあります。<br>おしゃれな店構えであるにもかかわらず、子供っぽさの象徴であるナルトを入れてしまう、自己中心的な、まるで西乃のようなあなたには注意が必要です。もう少し大人になる努力をしてみましょう。',
        },
        {
          id: 10,
          name: '三好',
          sentence: 'あなたは <b>三好</b> タイプ。<br>個性が何もなく、人間的な魅力が希薄であり、人生の楽しみを見つけにくいので、人生の充実感は薄いでしょう。特筆すべきことが何もない、そんな三好のようなあなたは注意が必要です。<br>よく分かんないけどとりあえずラウドバンドでも始めてみると尖ってくると思います。',
        },
      ],
    };
  },
  methods: {
    algoEgo(scores) {
      if ((scores['np'] > scores['cp']) && (Math.max(Object.values(scores)) === scores['np']) && (Math.min(Object.values(scores)) === Math.min([scores['cp'], scores['ac']])) && (scores['a'] >= scores['fc'] >= scores['ac'])) {
          return 1;
      } else if((Math.min(scores['np'], scores['ac']) >= scores['a']) && (Math.max(scores['cp'], scores['fc']) <= scores['a'])) {
          return 2;
      } else if ((Math.max(scores['np'], scores['ac']) <= scores['a']) && (Math.min(scores['cp'], scores['fc']) >= scores['a'])){
          return 3;
      } else if ((Math.min(scores['cp'], scores['ac']) >= scores['np']) && (Math.max(scores['a'], scores['fc']) <= scores['np'])){
        return 4;
      } else if (Math.min(scores['cp'], scores['a'], scores['ac']) >=Math.max(scores['np'], scores['fc'])){
          return 5;
      } else if (Math.min(scores['np'], scores['fc']) >=Math.max(scores['cp'], scores['a'], scores['ac'])){
          return 6;
      } else if ((scores['a'] >= Math.max(scores['np'], scores['fc'])) && (Math.min(scores['np'], scores['fc']) >= Math.max(scores['cp'], scores['ac']))){
        return 7;
      } else if (scores['cp'] >= scores['np'] >= scores['a'] >= scores['fc'] >= scores['ac']){
        return 8;
      } else if (scores['cp'] <= scores['np'] <= scores['a'] <= scores['fc'] <= scores['ac']){
        return 9;
      } else {
        return 10;
      }
    },
    ramenImgUrl(ramenId) {
      return `/ramenPictures/ramen_${ramenId}.jpg`;
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

  &::before {
    content: '';
    width: 1000px;
    height: 1000px;
    position: fixed;
    top: calc(50% - 500px);
    left: calc(50% - 500px);
    background-image: url('/logo.png');
    background-repeat: no-repeat;
    background-size: 100%;
    z-index: 0;
    opacity: 0.1;
  }

  &__contents {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  &__ramenName {
    font-size: 40px;
    font-weight: bold;
    margin: 20px auto;
  }

  &__ramenImage {
    display: block;
    width: 100%;
    margin: 30px auto;
    z-index: 1;
  }

  &__judgeSentence {
    line-height: 1.8em;
    margin: 30px auto;
  }

  &__toTopPage {
    display: block;
    margin: 70px auto 20px;
    z-index: 1;

    &__button {
      width: 200px;
      height: 50px;
      font-size: 15px;
    }
  }
}
</style>
