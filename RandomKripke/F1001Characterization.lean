import RandomKripke.FiniteFrames

namespace RandomKripke

/-- The target F1001 has an edge from every vertex to c. -/
theorem F1001_all_rows_hit_c (u : Fin 3) :
    F1001 u 0 = true := by
  fin_cases u <;> decide

/-- Rows over c or a have an edge to a. -/
theorem F1001_row_to_a (u : Fin 3) (h : u = 0 ∨ u = 1) :
    F1001 u 1 = true := by
  fin_cases u <;> simp_all [F1001]

/-- Rows over c or b have an edge to b. -/
theorem F1001_row_to_b (u : Fin 3) (h : u = 0 ∨ u = 2) :
    F1001 u 2 = true := by
  fin_cases u <;> simp_all [F1001]

/-- The only absent edges of F1001 are a→b and b→a. -/
theorem F1001_edge_of_not_cross (u v : Fin 3)
    (h : ¬ ((u = 1 ∧ v = 2) ∨ (u = 2 ∧ v = 1))) :
    F1001 u v = true := by
  fin_cases u <;> fin_cases v <;> simp_all [F1001]

/-- If an edge to a exists in F1001, its source is c or a. -/
theorem F1001_edge_to_a_implies_source (u : Fin 3)
    (h : F1001 u 1 = true) : u = 0 ∨ u = 1 := by
  fin_cases u <;> simp_all [F1001]

/-- If an edge to b exists in F1001, its source is c or b. -/
theorem F1001_edge_to_b_implies_source (u : Fin 3)
    (h : F1001 u 2 = true) : u = 0 ∨ u = 2 := by
  fin_cases u <;> simp_all [F1001]

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
      | false => rfl
      | true =>
          have h := hforth x y hxy
          simp [F1001, hx, hy] at h
    · intro x y hx hy
      cases hxy : R x y with
      | false => rfl
      | true =>
          have h := hforth x y hxy
          simp [F1001, hx, hy] at h
    · intro x
      obtain ⟨y, hxy, hy⟩ := hback x 0 (F1001_all_rows_hit_c (f x))
      exact ⟨y, hxy, hy⟩
    · intro x hx
      obtain ⟨y, hxy, hy⟩ := hback x 1 (F1001_row_to_a (f x) hx)
      exact ⟨y, hxy, hy⟩
    · intro x hx
      obtain ⟨y, hxy, hy⟩ := hback x 2 (F1001_row_to_b (f x) hx)
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
      · exact F1001_edge_of_not_cross (f x) (f y) hbad
    · intro x z htarget
      fin_cases z
      · exact hc x
      · have hclass := F1001_edge_to_a_implies_source (f x) htarget
        exact ha x hclass
      · have hclass := F1001_edge_to_b_implies_source (f x) htarget
        exact hb x hclass

end RandomKripke
