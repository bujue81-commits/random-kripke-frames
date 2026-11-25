import RandomKripke.FiniteFrames

namespace RandomKripke

/-- Boolean finite search for a surjective bounded morphism.
    Using Finset.any keeps the search computational, so exact counts
    can be checked by native_decide. -/
def HasBoundedImageBool {α β : Type}
    [Fintype α] [Fintype β] [DecidableEq β]
    (G : Frame α) (F : Frame β) : Bool :=
  (Finset.univ : Finset (α → β)).any
    (fun f => decide (IsBoundedMorphism G F f))

/-- All labelled three-point source relations admitting F0001 as an image. -/
def SourcesOfF0001OnThreePoints : Finset (Frame (Fin 3)) :=
  Finset.univ.filter (fun G =>
    HasBoundedImageBool G F0001 = true)

/-- All labelled three-point source relations admitting F1001 as an image. -/
def SourcesOfF1001OnThreePoints : Finset (Frame (Fin 3)) :=
  Finset.univ.filter (fun G =>
    HasBoundedImageBool G F1001 = true)

/-- Exact labelled count: the six relabellings of F0001. -/
theorem exact_count_F0001_n3 :
    SourcesOfF0001OnThreePoints.card = 6 := by
  native_decide

/-- Exact labelled count: the three distinct relabellings of F1001,
    accounting for its nontrivial automorphism swapping a and b. -/
theorem exact_count_F1001_n3 :
    SourcesOfF1001OnThreePoints.card = 3 := by
  native_decide

end RandomKripke
