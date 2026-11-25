import RandomKripke.FiniteFrames

namespace RandomKripke

/-- The fibrewise conditions for a surjective bounded morphism onto F1001.
The target vertices are ordered (c,a,b), and the three fibres are denoted
C,A,B respectively. -/
def F1001PartitionConditions {α : Type}
    (R : Frame α) (f : α → Fin 3) : Prop :=
  Function.Surjective f ∧
    (∀ x y, f x = 1 → f y = 2 → R x y = false) ∧
    (∀ x y, f x = 2 → f y = 1 → R x y = false) ∧
    (∀ x, ∃ y, R x y = true ∧ f y = 0) ∧
    (∀ x, f x = 0 ∨ f x = 1 →
      ∃ y, R x y = true ∧ f y = 1) ∧
    (∀ x, f x = 0 ∨ f x = 2 →
      ∃ y, R x y = true ∧ f y = 2)

/-- A map onto F1001 is a surjective bounded morphism exactly when:
(i) there are no edges from A to B or B to A;
(ii) every row hits C;
(iii) rows in C∪A hit A; and
(iv) rows in C∪B hit B. -/
theorem boundedMorphism_F1001_iff_partitionConditions
    {α : Type} (R : Frame α) (f : α → Fin 3) :
    IsBoundedMorphism R F1001 f ↔ F1001PartitionConditions R f := by
  constructor
  · rintro ⟨hs, hforth, hback⟩
    refine ⟨hs, ?_, ?_, ?_, ?_, ?_⟩
    · intro x y hx hy
      cases hxy : R x y with
      | false => exact hxy
      | true =>
          have h := hforth x y hxy
          simp [F1001, hx, hy] at h
    · intro x y hx hy
      cases hxy : R x y with
      | false => exact hxy
      | true =>
          have h := hforth x y hxy
          simp [F1001, hx, hy] at h
    · intro x
      have htarget : F1001 (f x) 0 = true := by
        fin_cases hfx : f x <;> simp [F1001, hfx]
      obtain ⟨y, hxy, hy⟩ := hback x 0 htarget
      exact ⟨y, hxy, hy⟩
    · intro x hx
      have htarget : F1001 (f x) 1 = true := by
        fin_cases hfx : f x <;> simp_all [F1001]
      obtain ⟨y, hxy, hy⟩ := hback x 1 htarget
      exact ⟨y, hxy, hy⟩
    · intro x hx
      have htarget : F1001 (f x) 2 = true := by
        fin_cases hfx : f x <;> simp_all [F1001]
      obtain ⟨y, hxy, hy⟩ := hback x 2 htarget
      exact ⟨y, hxy, hy⟩
  · rintro ⟨hs, hab, hba, hc, ha, hb⟩
    refine ⟨hs, ?_, ?_⟩
    · intro x y hxy
      by_cases hbad :
          (f x = 1 ∧ f y = 2) ∨ (f x = 2 ∧ f y = 1)
      · rcases hbad with ⟨hx, hy⟩ | ⟨hx, hy⟩
        · have hfalse := hab x y hx hy
          rw [hfalse] at hxy
          contradiction
        · have hfalse := hba x y hx hy
          rw [hfalse] at hxy
          contradiction
      · fin_cases hfx : f x <;> fin_cases hfy : f y <;>
          simp_all [F1001]
    · intro x z htarget
      fin_cases hz : z
      · simpa [hz] using hc x
      · have hclass : f x = 0 ∨ f x = 1 := by
          fin_cases hfx : f x <;> simp_all [F1001]
        simpa [hz] using ha x hclass
      · have hclass : f x = 0 ∨ f x = 2 := by
          fin_cases hfx : f x <;> simp_all [F1001]
        simpa [hz] using hb x hclass

end RandomKripke
