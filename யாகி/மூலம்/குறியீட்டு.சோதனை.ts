import { எண்ணிக்கை, புதிப்பு } from "@/குறியீட்டு.js";

describe("எண்ணிக்கை", function () {
  const எண்ணிக்கை_ = new எண்ணிக்கை({});

  describe("பதிப்பு", () => {
    expect(typeof புதிப்பு).toEqual("string");
  });

  describe("முறைமைகள் சோதனை", () => {
    test("கிடைக்கும் முறைமைகள் பின்கொடுக்க வேண்டும்", function () {
      expect(எண்ணிக்கை_.முறைமைகள்).toBeInstanceOf(Array);
      expect(எண்ணிக்கை_.முறைமைகள்.length).toBeGreaterThan(1);
    });
  });

  describe("உரைக்கு", function () {
    for (const முறைமை of எண்ணிக்கை_.முறைமைகள்) {
      test(முறைமை, function () {
        const எண் = 123.456;
        expect(
          எண்ணிக்கை_.எண்ணுக்கு({
            உரை: எண்ணிக்கை_.உரைக்கு({ எண், மொழி: முறைமை }),
            மொழி: முறைமை,
          })
        ).toEqual(எண்);
      });
    }
  });
});
