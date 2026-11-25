import RandomKripke.FiniteFrames

namespace RandomKripke

/-- Every point has a successor which is not reflexive. -/
def HasNonLoopSuccessorEverywhere {α : Type} (R : Frame α) : Prop :=
  ∀ x, ∃ y, R x y = true ∧ R y y = false

/-- Every ordered pair is joined by a path of exactly two edges. -/
def HasTwoStepReachability {α : Type} (R : Frame α) : Prop :=
  ∀ x z, ∃ y, R x y = true ∧ R y z = true

instance instDecidableHasNonLoopSuccessorEverywhere
    {α : Type} [Fintype α] (R : Frame α) :
    Decidable (HasNonLoopSuccessorEverywhere R) := by
  unfold HasNonLoopSuccessorEverywhere
  infer_instance

instance instDecidableHasTwoStepReachability
    {α : Type} [Fintype α] (R : Frame α) :
    Decidable (HasTwoStepReachability R) := by
  unfold HasTwoStepReachability
  infer_instance

/-- The three-point complete irreflexive directed frame. -/
def CompleteIrreflexive3 : Frame (Fin 3) :=
  fun x y => decide (x ≠ y)

/-- The two-point frame F_1 from Goranko (2020), Proposition 4.7:
0 is reflexive and central; 1 points only to 0. -/
def GorankoF1 : Frame (Fin 2) :=
  fun x y => if x.val = 0 then true else decide (y.val = 0)

/-- Collapse two irreflexive source points onto the central point 0,
and the third point onto the peripheral point 1. -/
def Collapse3toGorankoF1 : Fin 3 → Fin 2 :=
  fun x => if x.val = 2 then 1 else 0

/-- A finite counterexample to preservation of
∀x∃y(Rxy ∧ ¬Ryy) under surjective bounded morphisms.
Both source and target have two-step reachability (diameter at most 2). -/
theorem goranko_eta_not_preserved_counterexample :
    HasNonLoopSuccessorEverywhere CompleteIrreflexive3 ∧
    HasTwoStepReachability CompleteIrreflexive3 ∧
    IsBoundedMorphism CompleteIrreflexive3 GorankoF1 Collapse3toGorankoF1 ∧
    ¬ HasNonLoopSuccessorEverywhere GorankoF1 ∧
    HasTwoStepReachability GorankoF1 := by
  refine ⟨?_, ?_, ?_, ?_, ?_⟩
  · intro x
    fin_cases x
    · exact ⟨1, by decide, by decide⟩
    · exact ⟨0, by decide, by decide⟩
    · exact ⟨0, by decide, by decide⟩
  · intro x z
    fin_cases x <;> fin_cases z
    · exact ⟨1, by decide, by decide⟩
    · exact ⟨2, by decide, by decide⟩
    · exact ⟨1, by decide, by decide⟩
    · exact ⟨2, by decide, by decide⟩
    · exact ⟨0, by decide, by decide⟩
    · exact ⟨0, by decide, by decide⟩
    · exact ⟨1, by decide, by decide⟩
    · exact ⟨0, by decide, by decide⟩
    · exact ⟨0, by decide, by decide⟩
  · refine ⟨?_, ?_, ?_⟩
    · intro y
      fin_cases y
      · exact ⟨0, by decide⟩
      · exact ⟨2, by decide⟩
    · intro x y hxy
      fin_cases x <;> fin_cases y <;>
        simp_all [CompleteIrreflexive3, GorankoF1, Collapse3toGorankoF1]
    · intro x z htarget
      fin_cases x <;> fin_cases z
      · exact ⟨1, by decide, by decide⟩
      · exact ⟨2, by decide, by decide⟩
      · exact ⟨0, by decide, by decide⟩
      · exact ⟨2, by decide, by decide⟩
      · exact ⟨0, by decide, by decide⟩
      · simp [GorankoF1, Collapse3toGorankoF1] at htarget
  · intro h
    obtain ⟨y, hy, hloop⟩ := h 1
    fin_cases y <;> simp [GorankoF1] at *
  · intro x z
    refine ⟨0, ?_, ?_⟩
    · fin_cases x <;> decide
    · fin_cases z <;> decide

end RandomKripke
