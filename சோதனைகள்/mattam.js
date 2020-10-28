
var expect    = require("chai").expect
import { முறைமைகள், உரைக்கு, எண்ணுக்கு } from "../dist/வாடிகையாளர்"

describe("எண்ணிக்கை", function() {
  describe("முறைமைகள் சோதனை", function() {
    it("கிடைக்கும் முறைமைகள் பின்கொடுக்க வேண்டும்", function() {
      expect(முறைமைகள்).to.be.an("array").and.to.have.lengthOf.above(1)
    });
  });

  describe("உரைக்கு", function() {
    for (const முறைமை of முறைமைகள்) {
        it(முறைமை, function() {
            var எண் = 123.456
            expect(எண்ணுக்கு(உரைக்கு(எண், முறைமை), முறைமை)).to.equal(எண்)
        });
    }
  });
});