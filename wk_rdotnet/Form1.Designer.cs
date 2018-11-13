namespace wk_rdotnet
{
    partial class Form1
    {
        /// <summary>
        /// 必要なデザイナー変数です。
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// 使用中のリソースをすべてクリーンアップします。
        /// </summary>
        /// <param name="disposing">マネージ リソースを破棄する場合は true を指定し、その他の場合は false を指定します。</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows フォーム デザイナーで生成されたコード

        /// <summary>
        /// デザイナー サポートに必要なメソッドです。このメソッドの内容を
        /// コード エディターで変更しないでください。
        /// </summary>
        private void InitializeComponent()
        {
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.runToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.exampleOfNumericMatrixToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.exampleOfNumericVectorToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.exampleOfDataFrameToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.exampleOfFunctionToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.runToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(284, 24);
            this.menuStrip1.TabIndex = 0;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // runToolStripMenuItem
            // 
            this.runToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.exampleOfNumericMatrixToolStripMenuItem,
            this.exampleOfNumericVectorToolStripMenuItem,
            this.exampleOfDataFrameToolStripMenuItem,
            this.exampleOfFunctionToolStripMenuItem});
            this.runToolStripMenuItem.Name = "runToolStripMenuItem";
            this.runToolStripMenuItem.Size = new System.Drawing.Size(40, 20);
            this.runToolStripMenuItem.Text = "Run";
            // 
            // exampleOfNumericMatrixToolStripMenuItem
            // 
            this.exampleOfNumericMatrixToolStripMenuItem.Name = "exampleOfNumericMatrixToolStripMenuItem";
            this.exampleOfNumericMatrixToolStripMenuItem.Size = new System.Drawing.Size(217, 22);
            this.exampleOfNumericMatrixToolStripMenuItem.Text = "Example of NumericMatrix.";
            this.exampleOfNumericMatrixToolStripMenuItem.Click += new System.EventHandler(this.exampleOfNumericMatrixToolStripMenuItem_Click);
            // 
            // exampleOfNumericVectorToolStripMenuItem
            // 
            this.exampleOfNumericVectorToolStripMenuItem.Name = "exampleOfNumericVectorToolStripMenuItem";
            this.exampleOfNumericVectorToolStripMenuItem.Size = new System.Drawing.Size(217, 22);
            this.exampleOfNumericVectorToolStripMenuItem.Text = "Example of NumericVector.";
            this.exampleOfNumericVectorToolStripMenuItem.Click += new System.EventHandler(this.exampleOfNumericVectorToolStripMenuItem_Click);
            // 
            // exampleOfDataFrameToolStripMenuItem
            // 
            this.exampleOfDataFrameToolStripMenuItem.Name = "exampleOfDataFrameToolStripMenuItem";
            this.exampleOfDataFrameToolStripMenuItem.Size = new System.Drawing.Size(217, 22);
            this.exampleOfDataFrameToolStripMenuItem.Text = "Example of DataFrame.";
            this.exampleOfDataFrameToolStripMenuItem.Click += new System.EventHandler(this.exampleOfDataFrameToolStripMenuItem_Click);
            // 
            // exampleOfFunctionToolStripMenuItem
            // 
            this.exampleOfFunctionToolStripMenuItem.Name = "exampleOfFunctionToolStripMenuItem";
            this.exampleOfFunctionToolStripMenuItem.Size = new System.Drawing.Size(217, 22);
            this.exampleOfFunctionToolStripMenuItem.Text = "Example of Function.";
            this.exampleOfFunctionToolStripMenuItem.Click += new System.EventHandler(this.exampleOfFunctionToolStripMenuItem_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 261);
            this.Controls.Add(this.menuStrip1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Form1";
            this.Text = "Form1";
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem runToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem exampleOfNumericMatrixToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem exampleOfNumericVectorToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem exampleOfDataFrameToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem exampleOfFunctionToolStripMenuItem;
    }
}

