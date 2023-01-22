
import { முறைமைகள், உரைக்கு, எண்ணுக்கு } from "@/குறியீட்டு"

describe("எண்ணிக்கை", function() {
  describe("முறைமைகள் சோதனை", function() {
    test("கிடைக்கும் முறைமைகள் பின்கொடுக்க வேண்டும்", function() {
      expect(முறைமைகள்).toBeInstanceOf(Array)
      expect(முறைமைகள்.length).toBeGreaterThan(1)
    });
  });

  describe("உரைக்கு", function() {
    for (const முறைமை of முறைமைகள்) {
      test(முறைமை, function() {
            var எண் = 123.456
            expect(எண்ணுக்கு(உரைக்கு(எண், முறைமை), முறைமை)).toEqual(எண்)
        });
    }
  });
});