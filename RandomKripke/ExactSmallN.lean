import RandomKripke.FiniteFrames

namespace RandomKripke

/-- A source frame admits a surjective bounded morphism onto a target. -/
def AdmitsBoundedImage {α β : Type}
    (G : Frame α) (F : Frame β) : Prop :=
  ∃ f : α → β, IsBoundedMorphism G F f

/-- All labelled three-point source relations admitting F0001 as an image. -/
def SourcesOfF0001OnThreePoints : Finset (Frame (Fin 3)) :=
  Finset.univ.filter (fun G => AdmitsBoundedImage G F0001)

/-- All labelled three-point source relations admitting F1001 as an image. -/
def SourcesOfF1001OnThreePoints : Finset (Frame (Fin 3)) :=
  Finset.univ.filter (fun G => AdmitsBoundedImage G F1001)

/-- Exact labelled count: the six relabellings of F0001. -/
theorem exact_count_F0001_n3 :
    SourcesOfF0001OnThreePoints.card = 6 := by
  decide

/-- Exact labelled count: the three distinct relabellings of F1001,
    accounting for its nontrivial automorphism swapping a and b. -/
theorem exact_count_F1001_n3 :
    SourcesOfF1001OnThreePoints.card = 3 := by
  decide

end RandomKripke
