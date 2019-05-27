const defaultScore = {
  cp: null,
  np: null,
  a: null,
  fc: null,
  ac: null,
};

export const state = () => ({
  score: {
    cp: null,
    np: null,
    a: null,
    fc: null,
    ac: null,
  },
});

export const mutations = {
  setRawResult(_state, result) {
    _state.score.cp = result[0];
    _state.score.np = result[1];
    _state.score.a = result[2];
    _state.score.fc = result[3];
    _state.score.ac = result[4];
  },
  setInit(_state) {
    _state.score = defaultScore;
  },
};
