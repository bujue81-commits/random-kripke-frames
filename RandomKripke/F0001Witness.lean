import RandomKripke.FiniteFrames

namespace RandomKripke

/-- A weaker necessary event used in the F0001 first-moment argument.
The target vertices are ordered (c,a,b), and the fibres are C,A,B. -/
def F0001WitnessConditions {α : Type}
    (R : Frame α) (f : α → Fin 3) : Prop :=
  Function.Surjective f ∧
    (∀ x y, f x = 1 → f y = 1 → R x y = false) ∧
    (∀ x y, f x = 1 → f y = 2 → R x y = false) ∧
    (∀ x y, f x = 2 → f y = 1 → R x y = false) ∧
    (∀ x, f x = 1 → ∃ y, R x y = true ∧ f y = 0) ∧
    (∀ x, f x = 0 → ∃ y, R x y = true ∧ f y = 1)

/-- Every bounded morphism onto F0001 satisfies the weaker witness
conditions used for the F0001 first-moment upper bound. -/
theorem boundedMorphism_F0001_implies_witnessConditions
    {α : Type} (R : Frame α) (f : α → Fin 3) :
    IsBoundedMorphism R F0001 f → F0001WitnessConditions R f := by
  rintro ⟨hs, hforth, hback⟩
  refine ⟨hs, ?_, ?_, ?_, ?_, ?_⟩
  · intro x y hx hy
    cases hxy : R x y with
    | false => rfl
    | true =>
        have h := hforth x y hxy
        simp [F0001, hx, hy] at h
  · intro x y hx hy
    cases hxy : R x y with
    | false => rfl
    | true =>
        have h := hforth x y hxy
        simp [F0001, hx, hy] at h
  · intro x y hx hy
    cases hxy : R x y with
    | false => rfl
    | true =>
        have h := hforth x y hxy
        simp [F0001, hx, hy] at h
  · intro x hx
    have htarget : F0001 (f x) 0 = true := by
      rw [hx]
      decide
    obtain ⟨y, hxy, hy⟩ := hback x 0 htarget
    exact ⟨y, hxy, hy⟩
  · intro x hx
    have htarget : F0001 (f x) 1 = true := by
      rw [hx]
      decide
    obtain ⟨y, hxy, hy⟩ := hback x 1 htarget
    exact ⟨y, hxy, hy⟩

end RandomKripke
